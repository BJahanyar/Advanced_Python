import cv2
import numpy as np
 
my_camera = cv2.VideoCapture(0)

def filter01(frame):
	return cv2.bitwise_not(frame)
    

def filter02(frame):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rows, cols = frame_gray.shape
    half_frame = frame_gray[: , 0:cols//2 ]
    flipped_half_frame = cv2.flip(half_frame, 1)
    frame_gray[: , cols//2:] = flipped_half_frame 
    return frame_gray

def filter03(frame): 
    ret, frame = my_camera.read()
    height, width, _ = frame.shape
    zeros = np.zeros([height,width], dtype = "uint8")
    B, G, R = cv2.split(frame)
    image_red = cv2.merge([zeros, zeros, R])
    return image_red

def filter04(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    w , h = frame.shape
    roi = frame[w//2-150:w//2+150 ,h//2-150:h//2+150]
    frame_blur = cv2.blur(frame, (35,35))
    frame_blur [w//2-150:w//2+150 , h//2-150:h//2+150] = roi
    return frame_blur

def filter05 (frame):
    threshold_1 = 30
    threshold_2 = 80
    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.Canny(image_gray, threshold_1, threshold_2)

def filter06(frame):
    flipped = cv2.flip(frame, 0)
    return flipped

def filter07(frame):
    water_color = cv2.stylization(frame, sigma_s=60, sigma_r=0.6)
    return water_color

while True:
    validation, frame =  my_camera.read()
    if validation is not True:
        break
    
    cv2.imshow('original', frame)
    cv2.imshow('Webcam1', filter01(frame))
    cv2.imshow('Webcam2', filter02(frame))
    cv2.imshow('Webcam3', filter03(frame))
    cv2.imshow('Webcam4', filter04(frame))
    cv2.imshow('Webcam5', filter05(frame))
    cv2.imshow('Webcam6', filter06(frame))
    cv2.imshow('Webcam7', filter07(frame))
    
    cv2.waitKey(1)

#    if cv2.waitKey(1) & 0xFF == ord('s'):
#        cv2.imwrite('phot.jpg' , filter05(frame))
#        break
#
#my_camera.release()
#cv2.destroyAllWindows()