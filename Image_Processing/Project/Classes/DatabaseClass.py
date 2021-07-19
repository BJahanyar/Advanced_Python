#from _typeshed import Self
from sqlite3 import connect
from Classes.EmployeeClass import My_Employee

class My_Database:

    @staticmethod
    def insert(employee):
        query = f"INSERT INTO Employee(NationalId,FName,LName,BirthDate,PIC) VALUES('{employee.NationalID}','{employee.FName}','{employee.LName}','{employee.BDate}','{employee.PicPath}') "
        my_connection = connect('Database/MiniProjectDB.db')
        my_corsor = my_connection.cursor()
        my_corsor.execute(query)
        my_connection.commit()
        my_connection.close()



    @staticmethod
    def Get_All_Employees():
        my_connection = connect('Database/MiniProjectDB.db')
        my_corsor = my_connection.cursor()
        my_corsor.execute("SELECT * FROM Employee")
        DBResult = my_corsor.fetchall()       
        my_connection.close()
        result = []
        for item in DBResult:
            Temp = My_Employee()             
            Temp.NationalID = item[1]
            Temp.FName = item[2]
            Temp.LName = item[3]
            Temp.BDate = item[4]
            result.append(Temp)
        return result
        
    
