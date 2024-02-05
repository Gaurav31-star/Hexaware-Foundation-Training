from DBconnection import DBConnection
from Customers import Customers
class Orders(DBConnection):
   
    def __init__(self, order_id, customer_id,orderDate,TotalAmount):
      
        self.OrderID = order_id
        self.CustomerId=customer_id
        self.OrderDate = orderDate
        self.TotalAmount = TotalAmount
    
    def set_orderid(self,orderId):
        self.OrderID=orderId    
    def set_orderDate(self,orderDate):
        self.OrderDate=orderDate
    def set_Amount(self,Amount):
        self.TotalAmount=Amount
    def get_orderid(self):
        return self.OrderID
    def get_orderDate(self):
        return self.OrderDate
    def get_Amount(self):
        return self.TotalAmount

    def insert_new_order(self):
        try:
            self.open()
            self.c.execute(f"INSERT INTO Orders (OrderId,CustomerId,OrderDate,TotalAmount) VALUES ('{self.OrderID}','{self.CustomerId}','{self.OrderDate}','{self.TotalAmount}')")
            self.mydb.commit()
            self.customerId = self.c.lastrowid
            print(f"\nAdded order to database with ID: {self.OrderID}\n")
        except Exception as e:
            print(e)
        finally:
            self.close()
            return self.CustomerId              