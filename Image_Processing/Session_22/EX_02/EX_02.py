import cv2 
import numpy as np

images = [['x' for i in range(5)] for j in range(4)]

for i in range(4):
    for j in range(5):
        images[i][j] = cv2.imread(str(i + 1) + '/' + str(j + 1) + '.jpg') 
        images[i][j] = cv2.cvtColor(images[i][j], cv2.COLOR_BGR2GRAY)

result = [0 for i in range(4)]

for i in range(4):
    for j in range(5):
        result[i] += (images[i][j] / 5) 

full_image = np.zeros((2000, 2000), dtype=np.uint8)

full_image[0:1000, 0:1000] = result[0]
full_image[0:1000, 1000:2000] = result[1]
full_image[1000:2000, 0:1000] = result[2]
full_image[1000:2000, 1000:2000] = result[3]

cv2.imshow('Full_Image', full_image)
cv2.imwrite('Full_image.jpg', full_image)
cv2.waitKey()
