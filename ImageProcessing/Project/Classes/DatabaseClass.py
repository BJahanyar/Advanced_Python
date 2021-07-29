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
    def update(oldEmployeeId, employee):
        query = f"UPDATE Employee SET NationalId = '{employee.NationalID}', FName= '{employee.FName}', LName= '{employee.LName}', BirthDate= '{employee.BDate}', PIC= '{employee.PicPath}'  WHERE NationalId = '{oldEmployeeId}'"
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
            Temp.PicPath = item[5]
            result.append(Temp)
        return result
    
    @staticmethod
    def get_Employee_By_NationalId(nationalId):
        query = f"SELECT * FROM Employee WHERE NationalId = '{nationalId}'"
        my_connection = connect('Database/MiniProjectDB.db')
        my_corsor = my_connection.cursor()
        my_corsor.execute(query)
        DBResult = my_corsor.fetchall()       
        my_connection.close()
        if len(DBResult) == 0:
            return False
        else:
            result = My_Employee()             
            result.NationalID = DBResult[0][1]
            result.FName = DBResult[0][2]
            result.LName = DBResult[0][3]
            result.BDate = DBResult[0][4]
            result.PicPath = DBResult[0][5]
            return result
            
        
    
