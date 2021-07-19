from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget, QTableWidgetItem
from Classes.DatabaseClass import My_Database
from Classes.EmployeeClass import My_Employee

class MainWindow(QWidget):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        Loader = QUiLoader()
        self.ui = Loader.load("Forms/MainForm.ui")
        
        #Add Employee Button
        self.ui.AddEmployee_Register_Button.clicked.connect(self.AddEmployee_Register_Button)        
        self.ui.AddEmployee_Clear_Button.clicked.connect(self.AddEmployee_Clear_Button)

        #Edit Employee Button
        self.ui.EditEmployee_NationalIDSearch_Button.clicked.connect(self.EditEmployee_FindEmployee_Button)
        self.ui.EditEmployee_Save_Button.clicked.connect(self.EditEmployee_Save_Button)

        #List Employee Button
        self.ui.ListEmployee_List_Button.clicked.connect(self.ListEmployee_Button)
        self.ui.ListEmployee_Clear_Button.clicked.connect(self.ClearListEmployee_Button)
        self.ui.show()

    #***************** All Buttons *****************

    def AddEmployee_Register_Button(self):
        self.save_New_Employee()

    def AddEmployee_Clear_Button(self):
        self.AddEmployee_Clear_Form()

    def EditEmployee_FindEmployee_Button(self):
        self.disable_EditTab_Elements()
        nationalId = self.ui.findChild(QWidget, "Edit_NationalIDSearch_Edit" ).text()
        self.find_Employee(nationalId)

    def EditEmployee_Save_Button(self):
        currentNationalId = self.ui.findChild(QWidget, "Edit_NationalIDSearch_Edit" ).text()
        self.save_Changes(currentNationalId)

    def ListEmployee_Button(self):
        self.FillEmployeeListTable()

    #***************** Add Employee *****************

    def save_New_Employee(self):
        try:
            e = My_Employee
            e.FName = self.ui.findChild(QWidget, "Add_FirstName_Edit" ).text()
            e.LName = self.ui.findChild(QWidget, "Add_LastName_Edit" ).text()
            e.NationalID = self.ui.findChild(QWidget, "Add_NationalID_Edit" ).text()
            tempDate = str(self.ui.findChild(QWidget, "Add_BirthDate_Edit" ).date().getDate())
            tempDate = str.replace(tempDate,",","/")
            tempDate = tempDate[1:len(tempDate)-1].replace(" ","")
            e.BDate = tempDate
            e.PicPath = "C:/asasd/asdasd"
            My_Database.insert(e)
            self.AddEmployee_Clear_Form()
            return True
        except:
            return 0

    def AddEmployee_Clear_Form(self):
        self.ui.findChild(QWidget, "Add_FirstName_Edit" ).setText("")
        self.ui.findChild(QWidget, "Add_LastName_Edit" ).setText("")
        self.ui.findChild(QWidget, "Add_NationalID_Edit" ).setText("")

    #***************** Edit Employee *****************

    def clear_EditForm_Data(self):
        self.ui.findChild(QWidget, "Edit_NationalIDSearch_Edit" ).setText("")
        self.ui.findChild(QWidget, "Edit_FirstName_Edit").setText("")
        self.ui.findChild(QWidget, "Edit_LastName_Edit").setText("")
        self.ui.findChild(QWidget, "Edit_NationalID_Edit").setText("")

    def enable_EditTab_Elements(self):
        self.ui.findChild(QWidget, "Edit_FirstName_Edit").setDisabled(False)
        self.ui.findChild(QWidget, "Edit_LastName_Edit").setDisabled(False)
        self.ui.findChild(QWidget, "Edit_NationalID_Edit").setDisabled(False)
        self.ui.findChild(QWidget, "Edit_BirthDate_Edit").setDisabled(False)
        self.ui.findChild(QWidget, "pushButton_2").setDisabled(False)

    def disable_EditTab_Elements(self):
        self.ui.findChild(QWidget, "Edit_FirstName_Edit").setDisabled(True)
        self.ui.findChild(QWidget, "Edit_LastName_Edit").setDisabled(True)
        self.ui.findChild(QWidget, "Edit_NationalID_Edit").setDisabled(True)
        self.ui.findChild(QWidget, "Edit_BirthDate_Edit").setDisabled(True)
        self.ui.findChild(QWidget, "pushButton_2").setDisabled(True)

    def load_Employee_Data_To_Form(self, employee):
        self.ui.findChild(QWidget, "Edit_NationalID_Edit").setText(employee.NationalID) 
        self.ui.findChild(QWidget, "Edit_FirstName_Edit").setText(employee.FName)
        self.ui.findChild(QWidget, "Edit_LastName_Edit").setText(employee.LName)

    def find_Employee(self, nationalId):
        result = My_Database.get_Employee_By_NationalId(nationalId)
        if result:
            self.load_Employee_Data_To_Form(result)
            self.enable_EditTab_Elements()

    def save_Changes(self, currentNationalId):
        try:
            e = My_Employee
            e.FName = self.ui.findChild(QWidget, "Edit_FirstName_Edit" ).text()
            e.LName = self.ui.findChild(QWidget, "Edit_LastName_Edit" ).text()
            e.NationalID = self.ui.findChild(QWidget, "Edit_NationalID_Edit" ).text()
            tempDate = str(self.ui.findChild(QWidget, "Edit_BirthDate_Edit" ).date().getDate())
            tempDate = str.replace(tempDate,",","/")
            tempDate = tempDate[1:len(tempDate)-1].replace(" ","")
            e.BDate = tempDate
            e.PicPath = "C:/asasd/asdasd"
            My_Database.update(currentNationalId, e)
            self.clear_EditForm_Data()
            return True       
        except:
            return 0
    
    #***************** List Employee *****************

    def ClearListEmployee_Button(self):
        table = self.ui.findChild(QWidget, "EmployeesListTableWidget" )
        table.setRowCount(0)

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