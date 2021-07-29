import cv2

a = cv2.imread ('a.tif')
b = cv2.imread ('b.tif')

c = cv2.subtract (b , a)

cv2.imwrite ('c.jpg' , c)
cv2.imshow('output' , c) 
cv2.waitKey()
