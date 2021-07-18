from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QVBoxLayout
from Classes.DatabaseClass import My_Database

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
        self.addEmployeeWin = Loader.load("Forms/AddEmployeeForm.ui")
        self.addEmployeeWin.show()

    def openEditEmployeeForm(self):
        Loader = QUiLoader()  
        self.EditEmployeeWin = Loader.load("Forms/EditEmployeeForm.ui")
        self.EditEmployeeWin.show() 

    def openListEmployeeForm(self):
        self.FillTable()

    def FillTable(self):
        EmployeesList = My_Database.select()
        lenght = len(EmployeesList)
        
        table = self.ui.findChild(QWidget, "tableWidget")
        for Employee in EmployeesList:
            rowPosition = table.rowCount()
            table.insertRow(rowPosition)
            table.setItem(rowPosition,0, QTableWidgetItem(Employee[1]))
            table.setItem(rowPosition,1, QTableWidgetItem(Employee[2]))
            table.setItem(rowPosition,2, QTableWidgetItem(Employee[3]))
            table.setItem(rowPosition,3, QTableWidgetItem(Employee[4]))
        table.verticalHeader().setVisible(False)        

      

class addEmployeeWindows(QWidget):
    def __init__(self):
        super(addEmployeeWindows, self).__init__()

class listEmployeeWindows(QWidget):
    def __init__(self):
        super(listEmployeeWindows, self).__init__()
        self.ui.pushButton.clicked.connect(self.Test(self))


