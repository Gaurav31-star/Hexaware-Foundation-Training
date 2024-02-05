import mysql.connector as con

from DBconnection import DBConnection

class CustomerRepository(DBConnection):
    def __init__(self):
        pass

    def getCustomerByID(self, cid):
        try:
            self.open()
            self.c.execute(f"Select * From Customers Where CustomerId = {cid}")
            cust = self.c.fetchone()
        except Exception as e:
            print(e)
        finally:
            self.close()
            return False if cust == None or cust == [] else cust
  
    def show_all_products(self):
        #try:
            self.open()
            self.c.execute("SELECT ProductID, ProductName, Description, Price FROM Products")
            products = self.c.fetchall()
            if not products:
                print("No products found.")
            else:
                print("All Products:")
                for product in products:
                    product_id, product_name, description, price = product
                    print(f"Product ID: {product_id}, Product Name: {product_name}, Description: {description}, Price: {price}")
                    print() 
        #except Exception as e:
          #  print(e)
        #finally:
           # self.close() 

    def calculate_total_orders(self,customer_id):
        #try:
            self.open()  
            self.c.execute(f"SELECT COUNT(*) FROM Orders WHERE CustomerID = {customer_id}")
            total_orders = self.c.fetchone()[0]  
            print(f"Total orders placed by Customer ID {customer_id}: {total_orders}")
            return total_orders
        
        #except Exception as e:
         #   print(e)
        #finally:
         #   self.close()

    def getCustomerDetails(self,customer_id):
        #try:
            self.open() 
            self.c.execute(f"SELECT * FROM Customers WHERE CustomerID = {customer_id}")
            customer_details = self.c.fetchone()  
            if customer_details:
                print("Customer Details:")
                print(f"Customer ID: {customer_details[0]}")
                print(f"First Name: {customer_details[1]}")
                print(f"Last Name: {customer_details[2]}")
                print(f"Email: {customer_details[3]}")
                print(f"Phone: {customer_details[4]}")
                print(f"Address: {customer_details[5]}")
                
            else:
                print("Customer not found.")
        #except Exception as e:
         #   print(e)
        #finally:
         #   self.close() 

    def updateCustomerInfo(self,customer_id,new_email=None, new_phone=None, new_address=None):
        #try:
            self.open()  
            update_query = "UPDATE Customers SET "
            update_fields = []

            if new_email:
                update_fields.append(f"Email = '{new_email}'")
            if new_phone:
                update_fields.append(f"Phone = '{new_phone}'")
            if new_address:
                update_fields.append(f"Address = '{new_address}'")

            if not update_fields:
                print("No information provided for update.")
                return

            update_query += ", ".join(update_fields)
            update_query += f" WHERE CustomerID = {customer_id}"
            
            self.c.execute(update_query)
            self.mydb.commit()

            print("Customer information updated successfully.")
        #except Exception as e:
          #  print(e)
        #finally:
         #   self.close()                         
    
    def updateProductInfo(self, product_id, new_price=None, new_description=None):
        #try:
            self.open() 
            update_query = "UPDATE Products SET "
            update_fields = []

            if new_price:
                update_fields.append(f"Price = {new_price}")
            if new_description:
                update_fields.append(f"Description = '{new_description}'")

            if not update_fields:
                print("No information provided for update.")
                return

            update_query += ", ".join(update_fields)
            update_query += f" WHERE ProductID = {product_id}"
            
            self.c.execute(update_query)
            self.mydb.commit()

            print("Product information updated successfully.")
        #except Exception as e:
         #   print(e)
        #finally:
          #  self.close() 

    def is_product_in_stock(self, product_id):
        #try:
            self.open()  
            self.c.execute(f"SELECT QuantityInStock FROM Inventory WHERE ProductId = {product_id}")
            stock_quantity = self.c.fetchone()

            if stock_quantity:
                stock_quantity = stock_quantity[0] 
                if stock_quantity > 0:
                    print(f"Product with ID {product_id} is in stock. Available quantity: {stock_quantity}")
                    return True
                else:
                    print(f"Product with ID {product_id} is out of stock.")
                    return False
            else:
                print("Product not found in inventory.")
                return False
        #except Exception as e:
         #   print(e)
          #  return False
        #finally:
         #   self.close()   

    def calculate_total_amount(self,order_id):
       # try:
            self.open()  
            self.c.execute(f"SELECT od.Quantity * p.Price AS TotalPerProduct "
                           f"FROM OrderDetails od "
                           f"JOIN Products p ON od.ProductID = p.ProductID "
                           f"WHERE od.OrderID = {order_id}")
            total_amounts = self.c.fetchall()

            if total_amounts:
                total_amount = sum(total[0] for total in total_amounts)
                print(f"Total amount for Order ID {order_id}: {total_amount}")
                return total_amount
            else:
                print("No products found in the order.")
                return 0 
        #except Exception as e:
         #   print(e)
          #  return 0 
        #finally:
         #   self.close()  

    def get_order_details(self,order_id):
       # try:
            self.open() 
            self.c.execute(f"SELECT od.ProductID, p.ProductName, od.Quantity "
                           f"FROM OrderDetails od "
                           f"JOIN Products p ON od.ProductID = p.ProductID "
                           f"WHERE od.OrderID = {order_id}")
            order_details = self.c.fetchall()

            if order_details:
                print(f"Order Details for Order ID {order_id}:")
                for product_id, product_name, quantity in order_details:
                    print(f"Product ID: {product_id}, Product Name: {product_name}, Quantity: {quantity}")
            else:
                print("No details found for this order.")
        #except Exception as e:
        #    print(e)
        #finally:
         #   self.close()   

    def update_order_status(self, order_id,new_status):
       # try:
            self.open() 
            self.c.execute(f"UPDATE Orders SET Status = '{new_status}' WHERE OrderID = {order_id}")
            self.mydb.commit()

            print(f"Order status updated to '{new_status}' for Order ID {order_id}")
        #except Exception as e:
         #   print(e)
        #finally:
         #   self.close()  

    def cancel_order(self,order_id):
        #try:
            self.open()  
            self.c.execute(f"SELECT ProductID, Quantity FROM OrderDetails WHERE OrderID = {order_id}")
            order_details = self.c.fetchall()

            if order_details:
                for product_id, quantity in order_details:
                    self.c.execute(f"UPDATE inventory SET QuantityInStock = QuantityInStock + {quantity} WHERE ProductId = {product_id}")

               
                self.c.execute(f"UPDATE Orders SET Status = 'Canceled' WHERE OrderID = {order_id}")
                self.mydb.commit()

                print(f"Order with ID {order_id} has been canceled. Stock levels adjusted.")
            else:
                print("No details found for this order.")
        #except Exception as e:
         #   print(e)
        #finally:
         #   self.close()                   

    def update_quantity(self, new_quantity,order_detail_id):
        #try:
            self.open() 
            self.c.execute(f"UPDATE OrderDetails SET Quantity = {new_quantity} WHERE OrderDetailsId = {order_detail_id}")
            self.mydb.commit()

            print(f"Quantity updated to {new_quantity} for OrderDetail ID {order_detail_id}")
        #except Exception as e:
         #   print(e)
        #finally:
         #   self.close()   

    def add_to_inventory(self, product_id, quantity):
        #try:
            self.open()  
            self.c.execute(f"UPDATE inventory SET QuantityInStock = QuantityInStock + {quantity} WHERE ProductId = {product_id}")
            self.mydb.commit()

            print(f"Added {quantity} units of Product ID {product_id} to inventory.")
        #except Exception as e:
         #   print(e)
        #finally:
         #   self.close()  

    def remove_from_inventory(self, product_id, quantity):
        #try:
            self.open()  
            self.c.execute(f"UPDATE inventory SET QuantityInStock = QuantityInStock - {quantity} WHERE ProductId = {product_id}")
            self.mydb.commit()

            print(f"Removed {quantity} units of Product ID {product_id} from inventory.")
        #except Exception as e:
         #   print(e)
        #finally:
         #   self.close() 

    def update_stock_quantity(self, product_id, new_quantity):
        #try:
            self.open()  
            self.c.execute(f"UPDATE inventory SET QuantityInStock = {new_quantity} WHERE ProductId = {product_id}")
            self.mydb.commit()

            print(f"Stock quantity for Product ID {product_id} updated to {new_quantity}.")
        #except Exception as e:
         #   print(e)
        #finally:
         #   self.close()                            
    def is_product_available(self, product_id, quantity_to_check):
        #try:
            self.open() 
            self.c.execute(f"SELECT QuantityInStock FROM inventory WHERE ProductId = {product_id}")
            available_quantity = self.c.fetchone()

            if available_quantity:
                available_quantity = available_quantity[0]  
                if available_quantity >= quantity_to_check:
                    print(f"{quantity_to_check} units of Product ID {product_id} are available in the inventory.")
                    return True
                else:
                    print(f"Insufficient stock! Only {available_quantity} units of Product ID {product_id} available.")
                    return False
            else:
                print("Product not found in inventory.")
                return False
        #except Exception as e:
         #   print(e)
          #  return False
        #finally:
         #   self.close()  

    def list_low_stock_products(self, threshold):
        #try:
            self.open()  
            self.c.execute(f"SELECT i.ProductId, p.ProductName, i.QuantityInStock "
                           f"FROM inventory i "
                           f"JOIN Products p ON i.ProductId = p.ProductID "
                           f"WHERE i.QuantityInStock < {threshold}")
            low_stock_products = self.c.fetchall()

            if low_stock_products:
                print(f"Products with quantities below {threshold} (indicating low stock):")
                for product_id, product_name, quantity in low_stock_products:
                    print(f"Product ID: {product_id}, Product Name: {product_name}, Quantity: {quantity}")
            else:
                print(f"No products found with quantities below {threshold}.")
        #except Exception as e:
         #   print(e)
        #finally:
         #   self.close()

    def list_out_of_stock_products(self):
        #try:
            self.open()  
            self.c.execute("SELECT i.ProductId, p.ProductName "
                           "FROM inventory i "
                           "JOIN Products p ON i.ProductId = p.ProductID "
                           "WHERE i.QuantityInStock = 0")
            out_of_stock_products = self.c.fetchall()

            if out_of_stock_products:
                print("Products that are out of stock:")
                for product_id, product_name in out_of_stock_products:
                    print(f"Product ID: {product_id}, Product Name: {product_name}")
            else:
                print("No products found that are out of stock.")
        #except Exception as e:
         #   print(e)
        #finally:
         #   self.close()         