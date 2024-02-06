from DBPropertyUtil import PropertyUtil

import mysql.connector as connection

class DBConnection():
    def __init__(self):
        pass

    def open(self):
        try:
            l = PropertyUtil.getPropertyString()
            self.mydb = connection.connect(host=l[0], database=l[3], username=l[1], password=l[2])
            self.c = self.mydb.cursor(buffered = True)
        except Exception as e:
            print(e)
    
    def close(self):
        self.c.close()
