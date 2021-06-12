import cv2

############################

image = cv2.imread('4.jpg')
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
rows = image.shape[0]
cols = image.shape[1]

for i in range(rows):
    for j in range(cols):
        if image[i, j] < 50:
            image[i, j] = 0
        elif image[i, j] >= 50:
            image[i, j] = 255


cv2.imshow('Black & White', image)
cv2.waitKey()