from PySide6.QtUiTools import *
from PySide6.QtWidgets import *
from PySide6.QtCore import QThread, Signal, Slot, Qt 
from PySide6.QtGui import QPixmap
from PySide6 import QtGui
import numpy as np
import cv2


class My_Video(QThread):
    change_pixmap_signal = Signal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()

    @staticmethod
    def filter01(frame):
	    return cv2.bitwise_not(frame)
    
    @staticmethod
    def filter02(frame):
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rows, cols = frame_gray.shape
        half_frame = frame_gray[: , 0:cols//2 ]
        flipped_half_frame = cv2.flip(half_frame, 1)
        frame_gray[: , cols//2:] = flipped_half_frame 
        return frame_gray

    @staticmethod
    def filter03(frame): 
        height, width, _ = frame.shape
        zeros = np.zeros([height,width], dtype = "uint8")
        B, G, R = cv2.split(frame)
        image_red = cv2.merge([zeros, zeros, R])
        return image_red

    @staticmethod
    def filter04(frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        w , h = frame.shape
        roi = frame[w//2-150:w//2+150 ,h//2-150:h//2+150]
        frame_blur = cv2.blur(frame, (35,35))
        frame_blur [w//2-150:w//2+150 , h//2-150:h//2+150] = roi
        return frame_blur

    @staticmethod
    def filter05 (frame):
        threshold_1 = 30
        threshold_2 = 80
        image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.Canny(image_gray, threshold_1, threshold_2)

    @staticmethod
    def filter06(frame):
        flipped = cv2.flip(frame, 0)
        return flipped
   
    @staticmethod
    def filter07(frame): 
        height, width, _ = frame.shape
        zeros = np.zeros([height,width], dtype = "uint8")
        B, G, R = cv2.split(frame)
        image_green = cv2.merge([zeros, G, zeros])
        return image_green

    @staticmethod
    def filter08(frame): 
        height, width, _ = frame.shape
        zeros = np.zeros([height,width], dtype = "uint8")
        B, G, R = cv2.split(frame)
        image_blue = cv2.merge([B, zeros, zeros])
        return image_blue

class My_Pic:
    def faceDetection(image):
        result = ''
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray_image, 1.3)
        for i, face in enumerate(faces):
            x,y,w,h = face
            result = image[y:y+h, x:x+w ]
            cv2.imwrite("test.jpg", result)
            break
        return result