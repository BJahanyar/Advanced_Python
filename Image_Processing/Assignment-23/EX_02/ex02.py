import cv2
import numpy as np 
import matplotlib.pyplot as plt 

#**********************************************

def remove_white_border (image):
    rowSize = image.shape[0]
    colsize = image.shape[1]
    up_left = [-1,-1]
    down_right = [-1,-1]
    for row in range(rowSize):
        for col in range(colsize):
            if  up_left[0] > -1:
                if image[row,col] < 50 and (image[row-100,col] < 50) and (image[row,col-100] < 50):
                    down_right = [row,col]
            else:
                if (image[row,col] < 50) and (image[row,col+100] < 50) and (image[row+100,col] < 50):
                    up_left = [row,col]
    result = image [up_left[0]:down_right[0], up_left[1]:down_right[1] ]
    return result             



#************************************************************

img_sudoku = cv2.imread("C:\\Users\\Bahar\\sources\\repos\\Advanced_Python\\Image_Processing\\Session_23\\EX_02\\sudoku.tif") 
img_sudoku = cv2.cvtColor(img_sudoku, cv2.COLOR_BGR2GRAY)
hist  = cv2.calcHist ([img_sudoku] , [0] , None , [255] , [0, 255])

optimized = cv2.equalizeHist(img_sudoku)

Test1 = remove_white_border(optimized)
cv2.imwrite("final.jpg",Test1)





