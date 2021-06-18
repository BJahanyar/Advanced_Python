import cv2

img = cv2.imread ('mona_lisa.jpg')
img = cv2.cvtColor (img , cv2.COLOR_BGR2GRAY)

final = 

cv2.imshow('out',final)
cv2.waitKey()