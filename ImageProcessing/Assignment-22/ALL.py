############################### EX_01 ##############################

import cv2

a = cv2.imread ('a.tif')
b = cv2.imread ('b.tif')

c = cv2.subtract (b , a)

cv2.imwrite ('c.jpg' , c)
cv2.imshow('output' , c) 
cv2.waitKey()

############################### EX_02 ##############################

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

############################### EX_03 ##############################

import cv2

orgin = cv2.imread('board - origin.bmp')
test = cv2.imread('board - test.bmp')
orgin = cv2.cvtColor(orgin, cv2.COLOR_RGB2GRAY)
test = cv2.cvtColor(test, cv2.COLOR_RGB2GRAY)

orgin_flip = cv2.flip (orgin , 1 )


final = cv2.subtract (test , orgin_flip) * 30

cv2.imwrite ('final.jpg' , final )
cv2.imshow ('out', final)
cv2.waitKey()

############################### EX_04 ##############################

import cv2

img = cv2.imread('chess pieces.jpg') // 2 
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

rows = img.shape[0]
cols = img.shape[1]

begin = -1
end = -1
imgNumber = 1
for j in range (cols):
    if begin > -1 and end > -1:
        output = img[:,begin:end]
        cv2.imwrite( str(imgNumber) + ".jpg", output)
        cv2.imshow(str(imgNumber), output)
        imgNumber = imgNumber + 1
        begin = -1
        end = -1
    elif begin > -1:
        find = False
        for i in range (rows):
            if img[i,j]  < 120 :
                find = True
                break
        if find == False:
            end = j
    else:
        for i in range (rows):
            if img[i,j]  < 120 :
                begin = j
                break
cv2.waitKey()

################ EX_05 ###############

import cv2
import numpy as np

images = []
for i in range (1,15):
    img = cv2.imread(f'images/h{i}.jpg')
    img = cv2.cvtColor (img, cv2.COLOR_RGB2GRAY)
    images.append(img)

result = np.zeros (images[0].shape, dtype ='uint8')
 
for image in images:
    result += image // len(images)

cv2.imwrite ('result.jpg' , result)
cv2.imshow ('output' , result)
cv2.waitKey()

############################### EX_05 ##############################

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

cv2.imshow('out', mona_final) 
cv2.waitKey()

