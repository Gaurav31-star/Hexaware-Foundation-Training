from PropertyUtil import PropertyUtil

import mysql.connector as connection

class DBConnection():
    def _init_(self):
        pass

    def open(self):
        try:
            l = PropertyUtil.getPropertyString()
            self.mydb = connection.connect(host=l[0], username=l[1],password=l[2],database=l[3],port =l[4], auth_plugin=l[5])
            self.c = self.mydb.cursor(buffered = True)
        except Exception as e:
            print(e)
    
    def close(self):
        self.c.close()