from PySide6.QtCore import *
from PySide6.QtWidgets import *
import sys
 
class myLabel(QLabel):
    clicked = Signal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()
 
class Wind(QDialog):
    clicked = Signal()
    def __init__(self):
        super().__init__()
        self.label = myLabel()
        self.label.setText('This is a text label')
 
        vb = QVBoxLayout()
        vb.addWidget(self.label)
        self.setLayout(vb)
 
        self.label.clicked.connect(self.showData)
        self.clicked.connect(self.showData1)
 
    def showData(self):
        print('ok')
    def showData1(self):
        print('OOK')
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Wind()
    win.show()
    sys.exit(app.exec_())

