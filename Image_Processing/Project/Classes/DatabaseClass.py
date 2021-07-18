from sqlite3 import connect

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