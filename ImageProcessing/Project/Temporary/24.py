import cv2
import sys


from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import *
from PySide6.QtCore import QThread, Signal

class FaceDetector(QThread):
    signal_Success_Proccess =Signal()

    def __init__(self, image_path):
        super(FaceDetector, self).__init__()
        self.image_path = image_path
        
    def run(self): 
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
   
        image = cv2.imread(self.image_path)
        gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        faces = face_detector.detectMultiScale(gray_image, 1.3)

        for (x,y,w,h) in faces:
            cv2.rectangle(image, (x,y),(x+w,y+h), (0,0,255),8)

        cv2.imwrite('output.jpg',image)
        self.signal_Success_Proccess.emit()


class mainwindow(QWidget):
    def __init__(self):
        super(mainwindow, self).__init__()

        Loader = QUiLoader()
        self.ui = Loader.load("form.ui")
        self.ui.btn_browse.clicked.connect(self.openimage)
        self.ui.btn_start.clicked.connect(self.startFacedetection)

        self.ui.show()

    def openimage(self):
        image_path = QFileDialog.getOpenFileName(self, 'ax ra entekhab kon')
        self.image_path = image_path [0]
        my_pixmap = QPixmap(self.image_path)
        self.ui.label.setPixmap(my_pixmap)

    def startFacedetection(self):
        self.face_detector = FaceDetector(self.image_path)
        self.face_detector.start()
        self.face_detector.signal_Success_Proccess.connect(self.showoutput)

    def showoutput(self):
        my_pixmap = QPixmap("output.jpg")
        self.ui.label.setPixmap(my_pixmap)

if __name__ == "__main__":
    app = QApplication([])
    widget = mainwindow()
    sys.exit(app.exec_())

