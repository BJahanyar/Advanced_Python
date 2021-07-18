import sys
from PySide6.QtWidgets import QApplication
from Classes.FormClasses import MainWindow,addEmployeeWindows


app = QApplication([])
widget = MainWindow()
sys.exit(app.exec())
