import cv2
import numpy as np

bgr__image = cv2.imread('rubix.png')
rgb_image = cv2.cvtColor(bgr__image, cv2.COLOR_BGR2RGB)

Red = np.array([255, 0, 0])
Green = np.array([0, 255, 0])
Blue = np.array([0, 0, 255])
Cyan = np.array([0, 255, 255])
Magenta = np.array([255, 0, 255])
Yello = np.array([255, 255, 0])

Cyan_Pixel = cv2.inRange(rgb_image, Cyan, Cyan)
Yello_Pixel = cv2.inRange(rgb_image, Yello, Yello)
Magenta_Pixel = cv2.inRange(rgb_image, Magenta, Magenta)

rgb_image[Cyan_Pixel > 0] = Red
rgb_image[Yello_Pixel > 0] = Blue
rgb_image[Magenta_Pixel > 0] = Green

rgb_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
cv2.imwrite('Final_Rubik.png', rgb_image)