from DBproperty import PropertyUtil

import mysql.connector as connection

class DBConnection():
    def __init__(self):
        pass

    def open(self):
        try:
            l = PropertyUtil.getPropertyString()
            self.mydb = connection.connect(host='localhost', database='techshop', username='root', password='root',port='3306', auth_plugin='mysql_native_password')
            self.c = self.mydb.cursor(buffered = True)
        except Exception as e:
            print(e)
    
    def close(self):
        self.c.close()
