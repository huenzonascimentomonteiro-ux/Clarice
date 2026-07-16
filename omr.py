import cv2 as cv

# Def a function to load a img and turn it in binary one
def ld_img(path):
    image = cv.imread(path, cv.IMREAD_GRAYSCALE)
    _, image = cv.threshold(image, 127, 255, cv.THRESH_BINARY_INV)
    return image

# Read the image
image = ld_img(r"Parametro\gabarito.png")

# Split the image in 4 blocks, one for each subject
portugues = image[550:1420, 25:260]
matematica = image[550:1420, 282:517]
fisica = image[550:1420, 538:773]
quimica = image[550:1420, 798:1031]

# Get the contours of the first block (portugues)
contours, hierarchy = cv.findContours(
    portugues, 
    cv.RETR_TREE, 
    cv.CHAIN_APPROX_SIMPLE)

circular_contours = []

for contour in contours:
    area = cv.contourArea(contour)

    if area < 130:
        continue

    perimeter = cv.arcLength(contour, True)

    if perimeter == 0:
        continue

    circularity = 4 * 3.14159 * area / (perimeter * perimeter)

    if circularity > 0.8:
        circular_contours.append(contour)



letter_position = {
    65: "A",
    100: "B",
    140: "C",
    175: "D",
    210: "E"
}

# Find the x position of the center of each circular contour
x_positions = []
for contour in circular_contours:
    M = cv.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        x_positions.append(cx)

questions_marked = {}

i = 1
for x_pos in x_positions:
    cls_letter = min(letter_position.keys(), key=lambda k: abs(k - x_pos))
    questions_marked.update({f"{i}":f"{letter_position[cls_letter]}"})
    
    i += 1
print(questions_marked)


 