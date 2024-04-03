import cv2
import pytesseract

def extract_checkboxes(image_path):
    # Load the image
    image = cv2.imread(image_path)
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to extract binary image
    _, binary = cv2.threshold(grayscale, 200, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    checkboxes = []

    # Iterate through contours
    for contour in contours:
        # Calculate contour area
        area = cv2.contourArea(contour)

        # Filter out small contours (noise)
        if area > 100:
            x, y, w, h = cv2.boundingRect(contour)
            aspect_ratio = w / h

            # Check if contour has an aspect ratio close to 1 (square shape)
            if 0.9 < aspect_ratio < 1.1:
                checkboxes.append((x, y, w, h))

    # Sort checkboxes by y-coordinate
    checkboxes.sort(key=lambda checkbox: checkbox[1])

    # Extract checkbox options
    options = []
    for checkbox in checkboxes:
        x, y, w, h = checkbox
        option = ""
        # Check if the option is one line or two lines
        if h > 2 * w:
            # Two-line option
            option = grayscale[y:y+h//2, x:x+w]
        else:
            # One-line option
            option = grayscale[y:y+h, x:x+w]
        # Convert option to text
        _, option_binary = cv2.threshold(option, 200, 255, cv2.THRESH_BINARY_INV)
        option_text = pytesseract.image_to_string(option_binary, config='--psm 6')
        options.append(option_text.strip())

    return options

image_path = 'output\POC_RH18347Y_CAI_GUO_03122024_p3NaFW1_page_1.tif'
extracted_options = extract_checkboxes(image_path)
print(extracted_options)