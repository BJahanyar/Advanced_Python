#from _typeshed import Self
from sqlite3 import connect
from Classes.EmployeeClass import My_Employee

class My_Database:
    def insert():
        pass

    @staticmethod
    def select():
        my_connection = connect('Database/MiniProjectDB.db')
        my_corsor = my_connection.cursor()
        my_corsor.execute("SELECT * FROM Employee")
        result = my_corsor.fetchall()
        my_corsor.close
        return result

    def Get_All_Employees():
        DBResult = My_Database.select()
        result = []
        for item in DBResult:
            Temp = My_Employee()             
            Temp.NationalID = item[1]
            Temp.FName = item[2]
            Temp.LName = item[3]
            Temp.BDate = item[4]
            result.append(Temp)
        return result
    
