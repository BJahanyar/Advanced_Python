from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QDateEdit, QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QVBoxLayout
from Classes.DatabaseClass import My_Database
from Classes.EmployeeClass import My_Employee



class MainWindow(QWidget):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        Loader = QUiLoader()
        self.ui = Loader.load("Forms/MainForm.ui")
        self.ui.AddEmployee_Button.clicked.connect(self.AddEmployee_Button)        
        self.ui.EditEmployee_Button.clicked.connect(self.openEditEmployeeForm)

        self.ui.ListEmployee_Button.clicked.connect(self.ListEmployee_Button)
        self.ui.ClearListEmployee_Button.clicked.connect(self.ClearListEmployee_Button)
        self.ui.show()

    def AddEmployee_Button(self):
        e = My_Employee
        X = QDateEdit
        e.FName = self.ui.findChild(QWidget, "Add_FirstName_Edit" ).text()
        e.LName = self.ui.findChild(QWidget, "Add_LastName_Edit" ).text()
        e.NationalID = self.ui.findChild(QWidget, "Add_NationalID_Edit" ).text()
        tempDate = str(self.ui.findChild(QWidget, "Add_BirthDate_Edit" ).date().getDate())
        tempDate = str.replace(tempDate,",","/")
        tempDate = tempDate[1:len(tempDate)-1].replace(" ","")
        e.BDate = tempDate
        e.PicPath = "C:/asasd/asdasd"
        My_Database.insert(e)

    def openEditEmployeeForm(self):
        Loader = QUiLoader()  
        self.EditEmployeeWin = Loader.load("Forms/EditEmployeeForm.ui")
        self.EditEmployeeWin.show() 

    def ListEmployee_Button(self):
        self.FillEmployeeListTable()
        
    def ClearListEmployee_Button(self):
        table = self.ui.findChild(QWidget, "EmployeesListTableWidget" )
        X = QTableWidget
        #X.setRowCount(0)
        table.setRowCount(0)

    #****************************************************************
    
    def FillEmployeeListTable(self):
        table = self.ui.findChild(QWidget, "EmployeesListTableWidget" )
        table.setRowCount(0)
        EmployeesList = My_Database.Get_All_Employees()
        for item in EmployeesList:
            rowPosition = table.rowCount()
            table.insertRow(rowPosition)
            table.setItem(rowPosition, 0, QTableWidgetItem(item.NationalID))
            table.setItem(rowPosition, 1, QTableWidgetItem(item.FName))
            table.setItem(rowPosition, 2, QTableWidgetItem(item.LName))
            table.setItem(rowPosition, 3, QTableWidgetItem(item.BDate))
        table.verticalHeader().setVisible(False)

    #****************************************************************
