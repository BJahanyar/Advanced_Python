import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread ('mona_lisa.jpg') 
image = cv2.cvtColor (image , cv2.COLOR_BGR2GRAY)

(rows , cols) = image.shape

def get_gradient_2d(start, stop, width, height):
    return np.tile(np.linspace(start, stop, width), (height, 1))

gradient = get_gradient_2d(0,  255, cols, rows)
gradient = np.uint8(gradient)

mona_final = (image / gradient) 

cv2.imwrite('mona_final.jpg', mona_final)
cv2.imshow('out', mona_final) 
cv2.waitKey()