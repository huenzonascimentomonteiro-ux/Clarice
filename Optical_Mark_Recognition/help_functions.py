import cv2 as cv

def get_contours(image_name):
    # Load img;
    img = cv.imread(image_name, cv.IMREAD_GRAYSCALE)

    # Turn img in binary; 
    _, binary_img = cv.threshold(
        img,
        127,
        255,
        cv.THRESH_BINARY_INV
    )

    # Extract the contours from img;
    contours, _ = cv.findContours(
        binary_img,
        cv.RETR_LIST,
        cv.CHAIN_APPROX_SIMPLE
    )

    return contours
