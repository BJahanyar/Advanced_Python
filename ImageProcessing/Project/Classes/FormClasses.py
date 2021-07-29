from PySide6.QtWidgets import QLabel, QWidget, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget, QTableWidgetItem
from PySide6.QtCore import Slot, Qt 
from PySide6.QtGui import QPixmap
from PySide6 import QtGui
from numpy.lib.function_base import select
from Classes.DatabaseClass import My_Database
from Classes.EmployeeClass import My_Employee
from Classes.VideoClasses import My_Video, My_Pic
import numpy as np
import cv2

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        Loader = QUiLoader()
        self.ui = Loader.load("Forms/MainForm.ui")
        self.CameraForm = Loader.load("Forms/CameraForm.ui")
        self.disply_width = 640
        self.display_height = 480
        self.SelectedPicture = ""
        self.SelectedPicture_qt = ""
        self.SelectedPicture_nd = ""
        self.SelectedPicture_Crop = ""
        #Add Employee Button
        self.ui.AddEmployee_Register_Button.clicked.connect(self.AddEmployee_Register_Button)        
        self.ui.AddEmployee_Clear_Button.clicked.connect(self.AddEmployee_Clear_Button)
        self.ui.AddEmployee_Pic_Button.clicked.connect(self.AddEmployee_Pic_Button)

        #Edit Employee Button
        self.ui.EditEmployee_NationalIDSearch_Button.clicked.connect(self.EditEmployee_FindEmployee_Button)
        self.ui.EditEmployee_Save_Button.clicked.connect(self.EditEmployee_Save_Button)

        #List Employee Button
        self.ui.ListEmployee_List_Button.clicked.connect(self.ListEmployee_Button)
        self.ui.ListEmployee_Clear_Button.clicked.connect(self.ClearListEmployee_Button)
        self.ui.show()

        #CameraForm
        self.CameraForm.Camera_SavePicture_Button.clicked.connect(self.Camera_SavePicture_Button)

    #***************** All Buttons *****************

    def AddEmployee_Pic_Button(self):
        newForm = self.CameraForm
        newForm.Picture01 = newForm.findChild(QWidget, "Picture01")
        newForm.Picture02 = newForm.findChild(QWidget, "Picture02")
        newForm.Picture03 = newForm.findChild(QWidget, "Picture03")
        newForm.Picture04 = newForm.findChild(QWidget, "Picture04")
        newForm.Picture05 = newForm.findChild(QWidget, "Picture05")
        newForm.Picture06 = newForm.findChild(QWidget, "Picture06")
        newForm.Picture07 = newForm.findChild(QWidget, "Picture07")
        newForm.Picture08 = newForm.findChild(QWidget, "Picture08")
        newForm.Picture09 = newForm.findChild(QWidget, "Picture09")        
        newForm.Picture01.setScaledContents(True)
        newForm.Picture02.setScaledContents(True)
        newForm.Picture03.setScaledContents(True)
        newForm.Picture04.setScaledContents(True)
        newForm.Picture05.setScaledContents(True)
        newForm.Picture06.setScaledContents(True)
        newForm.Picture07.setScaledContents(True)
        newForm.Picture08.setScaledContents(True)
        newForm.Picture09.setScaledContents(True)

        newForm.thread = My_Video()
        newForm.thread.change_pixmap_signal.connect(self.update_image)
        newForm.thread.start()

        newForm.show()

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

    def Camera_SavePicture_Button(self):
        w = self.ui.findChild(QWidget, "Add_EmployeePicture_Label")
        self.SelectedPicture_Crop = My_Pic.faceDetection(self.SelectedPicture)        
        w.setPixmap(self.convert_cv_qt(self.SelectedPicture_Crop))
        w.setScaledContents(True)
        w.setVisible(True)
        self.CameraForm.close()
        
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
            e.PicPath = f"EmployeesPicture/{e.NationalID}.jpg"
            cv2.imwrite(f"EmployeesPicture/{e.NationalID}.jpg",self.SelectedPicture_Crop)
            My_Database.insert(e)
            self.AddEmployee_Clear_Form()
            return True
        except:
            return 0

    def AddEmployee_Clear_Form(self):
        self.ui.findChild(QWidget, "Add_FirstName_Edit" ).setText("")
        self.ui.findChild(QWidget, "Add_LastName_Edit" ).setText("")
        self.ui.findChild(QWidget, "Add_NationalID_Edit" ).setText("")
        self.ui.findChild(QWidget, "Add_EmployeePicture_Label" ).setVisible(False)
  
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
        w = self.ui.findChild(QWidget, "Edit_EmployeePicture_Label")
        image = cv2.imread(employee.PicPath)
        w.setPixmap(self.convert_cv_qt(image))
        w.setScaledContents(True)
        w.setVisible(True)        

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
            #X = QTableWidgetItem
            #tableItem = QTableWidgetItem
            #tableItem.setIcon(f"EmployeesPicture/{item.NationalID}.jpg")
            #table.setItem(rowPosition, 0, QTableWidgetItem(tableItem))            
            table.setItem(rowPosition, 1, QTableWidgetItem(item.NationalID))
            table.setItem(rowPosition, 2, QTableWidgetItem(item.FName))
            table.setItem(rowPosition, 3, QTableWidgetItem(item.LName))
            table.setItem(rowPosition, 4, QTableWidgetItem(item.BDate))
        table.verticalHeader().setVisible(False)

    #***************** Camera *****************

    @Slot(np.ndarray)
    def update_image(self, cv_img):
        self.SelectedPicture = cv_img
        self.SelectedPicture_qt = self.convert_cv_qt(cv_img)

        self.CameraForm.Picture01.setPixmap(self.convert_cv_qt(My_Video.filter01(cv_img)))
        self.CameraForm.Picture02.setPixmap(self.convert_cv_qt(My_Video.filter02(cv_img)))
        self.CameraForm.Picture03.setPixmap(self.convert_cv_qt(My_Video.filter03(cv_img)))
        self.CameraForm.Picture04.setPixmap(self.convert_cv_qt(My_Video.filter04(cv_img)))
        self.CameraForm.Picture05.setPixmap(self.convert_cv_qt(cv_img))
        self.CameraForm.Picture06.setPixmap(self.convert_cv_qt(My_Video.filter05(cv_img)))
        self.CameraForm.Picture07.setPixmap(self.convert_cv_qt(My_Video.filter06(cv_img)))
        self.CameraForm.Picture08.setPixmap(self.convert_cv_qt(My_Video.filter07(cv_img)))
        self.CameraForm.Picture09.setPixmap(self.convert_cv_qt(My_Video.filter08(cv_img)))    

    def convert_cv_qt(self, cv_img):    
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)