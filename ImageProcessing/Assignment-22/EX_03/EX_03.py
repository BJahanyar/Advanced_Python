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