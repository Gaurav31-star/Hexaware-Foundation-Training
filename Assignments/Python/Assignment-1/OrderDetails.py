
from DBconnection import DBConnection

class OrderDetails(DBConnection):
    def __init__(self,orderdetail_id,order_id,product_id,quantity):
        self.OderDetailId=orderdetail_id
        self.OrderId=order_id
        self.ProductId=product_id
        self.Quantity=quantity

    def insert_new_orderdetails(self):
        try:
            self.open()
            self.c.execute(f"INSERT INTO OrderDetails (OrderDetailsId,OrderId,ProductId,Quantity) VALUES ('{self.OderDetailId}','{self.OrderId}','{self.ProductId}', '{self.Quantity}')")
            self.mydb.commit()
            self.customerId = self.c.lastrowid
            print(f"\nOderdetails added with ID: {self.OderDetailId}\n")
            print(f"\nOrder Placed successfully\n")
        except Exception as e:
            print(e)
        finally:
            self.close()
            return self.OderDetailId      

  