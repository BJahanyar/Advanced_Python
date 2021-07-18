import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtUiTools import QUiLoader
from sqlite3 import connect

class Database:
    def insert():
        pass

    @staticmethod
    def select():
        my_connection = connect("MiniProjectDB")
        my_corsor = my_connection.cursor()
        my_corsor.execute("SELECT * FROM Employee")
        result = my_corsor.fetchall
        my_corsor.close
        return result

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        Loader = QUiLoader()
        self.ui = Loader.load("Image_Processing/Project/Forms/MainForm.ui")
        self.ui.AddEmployee_Button.clicked.connect(self.openAddEmployeeForm)
        label = QLabel()
        

        self.ui.show()

    def openAddEmployeeForm(self):
        w = addEmployeeWindows()
        w.show()

class addEmployeeWindows(QWidget):
    def __init__(self):
        super(addEmployeeWindows, self).__init__()
        Loader = QUiLoader()
        self.ui = Loader.load("Image_Processing/Project/Forms/AddEmployeeForm.ui")
        self.ui.show()

if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    sys.exit(app.exec())
