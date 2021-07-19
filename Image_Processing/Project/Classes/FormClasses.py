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
        self.FillEmployeeListTable()

    #****************************************************************
    
    def FillEmployeeListTable(self):
        table = self.ui.findChild(QWidget, "tableWidget" )
        EmployeesList = My_Database.Get_All_Employees()
        for item in EmployeesList:
            rowPosition = table.rowCount()
            table.insertRow(rowPosition)
            table.setItem(rowPosition, 0, QTableWidgetItem(item.NationalID))
            table.setItem(rowPosition, 1, QTableWidgetItem(item.FName))
            table.setItem(rowPosition, 2, QTableWidgetItem(item.LName))
            table.setItem(rowPosition, 3, QTableWidgetItem(item.BDate))
        table.verticalHeader().setVisible(False)