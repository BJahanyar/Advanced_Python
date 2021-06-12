import cv2

#########################

Image = cv2.imread('3.jpg')

rotated = cv2.rotate(Image, cv2.ROTATE_180)

cv2.imshow('Rotated Image', rotated)
cv2.waitKey()
