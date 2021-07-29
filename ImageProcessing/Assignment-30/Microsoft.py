import cv2
import matplotlib.pyplot as plt
from PIL import ImageFont
import numpy as np

image=np.zeros((156,352,3),dtype=np.uint8)

image[:,:]=[73,73,73] #BackGround
image[52:77,52:77]=[34,80,242] #Red
image[52:77,80:105]=[0,186,127] #Green
image[80:105,52:77]=[239,164,0] #Blue
image[80:105,80:105]=[0,185,255] #Yellow

cv2.putText(image, "MICROSOFT", (115,87), cv2.FONT_HERSHEY_TRIPLEX, 1, (255,255,255), 2 )
cv2.imwrite("Microsoft.jpg", image)
