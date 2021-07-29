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
