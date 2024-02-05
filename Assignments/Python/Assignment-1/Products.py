from DBconnection import DBConnection
class Products(DBConnection):
    def __init__(self, product_id, product_name, description, price):
        self.ProductID = product_id
        self.ProductName = product_name
        self.Description = description
        self.Price = price
        
    def set_productName(self,product_name):
        self.ProductName=product_name

    def set_description(self,description):
        self.Description=description

    def set_price(self,price):
        self.Price=price 

    def get_productName(self):
        return self.ProductName
    def get_description(self):
        return self.Description
    def get_price(self):
        return self.Price
              
    def GetProductDetails(self):
       print()
       print(f"ProductId: {self.ProductID}")
       print(f"ProductName: {self.ProductName}")
       print(f"Description: {self.Description}")
       print(f"Price: {self.Price}")
       print()

    def insert_new_products(self):
        try:
            self.open()
            self.c.execute(f"INSERT INTO products (ProductName,Description,Price) VALUES ('{self.ProductName}','{self.Description}', '{self.Price}')")
            self.mydb.commit()
            self.ProductID = self.c.lastrowid
            print(f"\nProduct '{self.ProductName}' added to the database with ID: {self.ProductID}\n")
        except Exception as e:
            print(e)
        finally:
            self.close()
            return self.ProductID
   
      