import cv2
import numpy as np

############################

rows = 800
cols = 800

chess = np.ones((rows, cols), np.uint8) * 255

for i in range (rows):
    for j in range (cols):
        if (i // 100) % 2 == 0:
            if (j//100) % 2 == 1:
             chess [ i , j ] = 0
        else:
            if (j//100) % 2 == 0:
             chess [ i , j ] = 0

cv2.imshow('Created Chess',chess)
cv2.waitKey()
