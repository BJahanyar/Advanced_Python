from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        Loader = QUiLoader()
        self.ui = Loader.load("Forms/MainForm.ui")
        self.ui.AddEmployee_Button.clicked.connect(self.openAddEmployeeForm)        
        self.ui.EditEmployee_Button.clicked.connect(self.openEditEmployeeForm)
        self.ui.ListEmployee_Button.clicked.connect(self.openListEmployeeForm)
        self.ui.show()

    def openAddEmployeeForm(self):
        Loader = QUiLoader()  
        self.addWmployeeWin = Loader.load("Forms/AddEmployeeForm.ui")
        self.addWmployeeWin.show()

    def openEditEmployeeForm(self):
        Loader = QUiLoader()  
        self.addWmployeeWin = Loader.load("Forms/EditEmployeeForm.ui")
        self.addWmployeeWin.show() 

    def openListEmployeeForm(self):
        Loader = QUiLoader()  
        self.addWmployeeWin = Loader.load("Forms/ListEmployeeForm.ui")
        self.addWmployeeWin.show()                

class addEmployeeWindows(QWidget):
    def __init__(self):
        super(addEmployeeWindows, self).__init__()

class listEmployeeWindows(QWidget):
    def __init__(self):
        super(listEmployeeWindows, self).__init__()
        layout = QtGui.QGridLayout() 
        self.table = QtGui.QTableWidget()
        self.table.setRowCount(20)
        self.table.setColumnCount(3)
        layout.addWidget(self.table)

        self.enterDataInTable()

        self.setLayout(layout)

    def enterDataInTable(self):  
        for row in range(0,20):
            for column in range(0,3):
                self.table.setItem(row, column, QtGui.QTableWidgetItem("cell %s-%s"%(row+1,column+1)))   
