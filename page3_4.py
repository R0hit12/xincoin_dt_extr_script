import os
import cv2
import numpy as np
from PIL import Image

from skimage import io
from skimage import morphology
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from matplotlib.figure import Figure

from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import easyocr

def checkbox_3and4(content_file_path):
    checkbox_content = []
    reader = easyocr.Reader(['en'])

    black = np.array([0, 0, 0])
    im = cv2.imread(content_file_path)
    org_im = im
    imshow(im)

    grayscale_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    imshow(grayscale_im)

    im_bin = cv2.adaptiveThreshold(grayscale_im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 5)

    im_bin = 255 - im_bin
    imshow(im_bin)

    selem_horizontal = morphology.rectangle(2, 8)
    im_filtered = morphology.closing(im_bin, selem_horizontal)

    selem_vertical = morphology.rectangle(8, 2)
    im_filtered = morphology.closing(im_bin, selem_vertical)


    im_filtered = im_filtered.astype(np.uint8)
    plt.imshow(im_filtered)
    kernel_h = np.ones((8, 5), np.uint8)
    kernel_v = np.ones((5, 8), np.uint8)

    im_bin_h = cv2.morphologyEx(im_filtered, cv2.MORPH_OPEN, kernel_h)

    Figure()
    plt.imshow(im_bin_h)

    im_bin_v = cv2.morphologyEx(im_filtered, cv2.MORPH_OPEN, kernel_v)

    Figure()
    plt.imshow(im_bin_v)

    im_final = im_bin_h | im_bin_v

    dilation_kernel = np.ones((1, 7), np.uint8)
    im_dilated = cv2.dilate(im_final, dilation_kernel, iterations=1)

    dilation_kernel = np.ones((7, 1), np.uint8)
    im_dilated = cv2.dilate(im_dilated, dilation_kernel, iterations=1)

    im_final = im_dilated
    Figure()
    imshow(im_final)

    imlabel = morphology.label(im_final)
    ar3 = imlabel > 0
    c = morphology.remove_small_objects(ar3, 5000, connectivity=8)
    Figure()
    imshow(c)

    [m, n] = np.shape(im_final)


    D = np.zeros((m, n), dtype='uint8')
    for i in range(m):
        for j in range(n):
            if c[i, j] == True:
                D[i, j] = 0
            else:
                D[i, j] = im_final[i, j]
    # Image.fromarray(D).show()

    # Get the properties of each region
    props = regionprops(imlabel)

    # Initialize an empty list to store the largest white areas and their corresponding bounding boxes
    largest_areas = []

    # Loop through each region
    for prop in props:
        # If the area of the region is larger than a certain threshold
        if prop.area > 1000:
            # Append the region's area and bounding box to the list
            largest_areas.append((prop.area, prop.bbox))

    # Sort the list in ascending order based on the top coordinate of the bounding box
    largest_areas.sort(key=lambda x: x[1][0])

    # Loop through each item in the list
    for area, bbox in largest_areas:
        # Extract the bounding box from the image
        minr, minc, maxr, maxc = bbox
        # Extend the bounding box by 100 pixels to the right
        width = maxc - minc
        height = maxr - minr

        if width > 500:
            # Check where black is more concentrated
            roi_black = im[minr:minr+30, minc:minc+180]
            black_pixels = np.sum(np.all(roi_black == black, axis=2))
            total_pixels = roi_black.shape[0] * roi_black.shape[1]
            concentration = black_pixels / total_pixels

            # Get the x and y coordinates of black pixels
            black_indices = np.where(np.all(roi_black == black, axis=2))
            x_coordinates = black_indices[1] + minc
            y_coordinates = black_indices[0] + minr

            # Display the bounding box in a separate window
            # fig, ax = plt.subplots(1)
            # ax.imshow(roi_black)
            # rect = patches.Rectangle((minc, minr), minc+180 - minc, minr+30 - minr, fill=False, edgecolor='red', linewidth=2)
            # ax.add_patch(rect)
            # plt.show()

            roi_gray = cv2.cvtColor(roi_black, cv2.COLOR_BGR2GRAY)
            _, roi_binary = cv2.threshold(roi_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

            if x_coordinates[0] in [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]:
                result = reader.readtext(roi_binary, detail=0)
                try:
                    if len(result) > 1:
                        print("No")
                except IndexError:
                    pass
            else:
                result = reader.readtext(roi_binary, detail=0)
                try:
                    text = result[0]
                    checkbox_content.append(text)
                    print(text)
                except IndexError:
                    pass

        else:
            maxc += 50
            # minr -= 100
            # minc -= 50
            roi = im[minr:maxr, minc:maxc]

            # Display the bounding box in a separate window
            # fig, ax = plt.subplots(1)
            # ax.imshow(roi)
            # rect = patches.Rectangle((minc, minr), maxc - minc, maxr - minr, fill=False, edgecolor='red', linewidth=2)
            # ax.add_patch(rect)
            # plt.show()

            roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            _, roi_binary = cv2.threshold(roi_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

            result = reader.readtext(roi_binary, detail=0)

            text = result[0]
            checkbox_content.append(text)
            # print(text)
    return checkbox_content
