import cv2
import numpy as np

from skimage import morphology
import matplotlib.pyplot as plt
from skimage.io import imshow
from matplotlib.figure import Figure
import easyocr

reader = easyocr.Reader(['en'])
checkbox_content = []
black = np.array([0, 0, 0])
im = cv2.imread('output\POC_RH18347Y_CAI_GUO_03122024_p3NaFW1_page_2.tif')
org_im = im
imshow(im)
# im = cv2.GaussianBlur(im, (3, 3), 0)
# Convert original image to grayscale
grayscale_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# cv2.imshow("Gray", grayscale_im)
imshow(grayscale_im)

im_bin = cv2.adaptiveThreshold(grayscale_im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 5)

im_bin = 255 - im_bin
imshow(im_bin)


# im_bin= morphology.thin(im_bin)

# Fill horizontal gaps, 8 pixels wide
selem_horizontal = morphology.rectangle(2, 8)
im_filtered = morphology.closing(im_bin, selem_horizontal)

# Fill vertical gaps, 8 pixels wide
selem_vertical = morphology.rectangle(8, 2)
im_filtered = morphology.closing(im_bin, selem_vertical)


im_filtered = im_filtered.astype(np.uint8)
plt.imshow(im_filtered)

# Kernel used to detect all the horisontal lines
kernel_h = np.ones((20, 1), np.uint8)

# Kernel to detect all the vertical lines
kernel_v = np.ones((1, 20), np.uint8)

# Horizontal kernel on the image
im_bin_h = cv2.morphologyEx(im_filtered, cv2.MORPH_OPEN, kernel_h)
# Image.fromarray(img_bin_h).show()
Figure()
plt.imshow(im_bin_h)
# Verical kernel on the image
im_bin_v = cv2.morphologyEx(im_filtered, cv2.MORPH_OPEN, kernel_v)
# Image.fromarray(img_bin_v).show()
Figure()
plt.imshow(im_bin_v)
# Combining the image
im_final = im_bin_h | im_bin_v
# Apply dilation on our image, to fill potential small gaps
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

# Initialize variables to store the largest white areas and their corresponding bounding boxes
largest_areas = []
largest_areas_bboxes = []

# Find all connected components
_, labels, stats, _ = cv2.connectedComponentsWithStats(D, connectivity=4, ltype=cv2.CV_32S)

for x, y, w, h, area in stats[2:]:
    # Extract the white area from the image
    white_area = D[y:y+h, x:x+w]
    
    # Check if the current white area is larger than a threshold
    if area > 450:
        # Add the white area and its bounding box to the list of largest areas
        largest_areas.append(white_area)
        largest_areas_bboxes.append((x, y, w, h))

# Sort the largest areas in ascending order based on the top coordinate of the bounding box
largest_areas_bboxes.sort(key=lambda bbox: bbox[1])

# Check if any largest white areas were found
if len(largest_areas) > 0:
    # Show all the largest white areas with a particular height
    for i in range(len(largest_areas)):
        # Check if the white area has a specific height
        if largest_areas_bboxes[i][3] < 35:
            # Check if the white area contains yellow pixels
            yellow_pixels = np.where(largest_areas[i] == 255)
            if len(yellow_pixels[0]) > 0:
                # Calculate the area of the yellow portion
                yellow_area = len(yellow_pixels[0])
                if yellow_area > 740:
                    # Show the portion of the original image extended by 100px to the right
                    extended_area = org_im[largest_areas_bboxes[i][1]:largest_areas_bboxes[i][1]+largest_areas_bboxes[i][3], largest_areas_bboxes[i][0]:largest_areas_bboxes[i][0]+largest_areas_bboxes[i][2]+300]
                    # plt.imshow(extended_area)
                    # plt.show()
                    roi_gray = cv2.cvtColor(extended_area, cv2.COLOR_BGR2GRAY)
                    _, roi_binary = cv2.threshold(roi_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

                    result = reader.readtext(roi_binary, detail=0)
                    try:
                        print(result)
                        checkbox_content.append(result)
                    except IndexError:
                        pass
# checkbox_content = [' ',join(sublist) for sublist in checkbox_content]
checkbox_content = [' '.join(sublist) for sublist in checkbox_content]                    
print(checkbox_content)