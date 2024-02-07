import mysql.connector 
from datetime import datetime
from DBConnection import DBConnection
    
class serviceprovider(DBConnection):
    
    def create_product(self, name, price,description,stockQuantity):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="ecommerce",port="3306",auth_plugin='mysql_native_password')
        try: 
            query = f"INSERT INTO products (name, price,description,stockQuantity) VALUES ('{name}', '{price}','{description}', '{stockQuantity}')"
            c = con.cursor()
            c.execute(query)
            con.commit()
            product_id = c.lastrowid
            print(f"\nProduct '{name}' added to the database with ID: {product_id}\n")
            return product_id
        except Exception as e:
            print(e)
            return False
        finally:
            con.close()

    def create_customer(self, name, email, password):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="ecommerce",port="3306",auth_plugin='mysql_native_password')
        try:
            query = f"INSERT INTO customers (name, email, password) VALUES ('{name}', '{email}', '{password}')"
            c = con.cursor()
            c.execute(query)
            con.commit()
            customer_id = c.lastrowid
            print(f"\nCustomer '{name}' added to the database with ID: {customer_id}\n")
            return customer_id
        except Exception as e:
            print(e)
            return None
        finally:
            pass 

    def customer_exists(self, name, password):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="ecommerce",port="3306",auth_plugin='mysql_native_password')
        try:
            query = f"SELECT COUNT(*) FROM customers WHERE name = '{name}' AND password = '{password}'"
            c = con.cursor()
            c.execute(query)
            con.commit()
            #self.c.execute(query)
            count = c.fetchone()[0]  
            return count
        except Exception as e:
            print(e)
            return False
        finally:
            pass
        
    def delete_product(self,product_id):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="ecommerce",port="3306",auth_plugin='mysql_native_password')
        try:
            query = f"DELETE FROM products WHERE product_id = {product_id}"
            c = con.cursor()
            c.execute(query)
            con.commit()
            if c.rowcount > 0:
                print(f"Product with ID: {product_id} deleted successfully.")
            else:
                print(f"No product found with ID: {product_id}. Nothing was deleted.")
            return False
        except Exception as e:
            print(e)
            return None
        finally:
            pass
        
    def delete_customer(self, customer_id):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="ecommerce",port="3306",auth_plugin='mysql_native_password')
        try:
            query = f"DELETE FROM customers where customer_id = {customer_id}"
            c= con.cursor()
            c.execute(query)
            con.commit()
            if c.rowcount > 0:
                print(f"Customer with ID: {customer_id} deleted successfully.")
            else:
                print(f"No customer found with ID: {customer_id}. Nothing was deleted.")
            return False
        except Exception as e:
            print(e)
            return None
        finally:
            pass
        
    def addTocart(self,customer_id,product_id, quantity):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="ecommerce",port="3306",auth_plugin='mysql_native_password')
        try:
            query = f"INSERT INTO cart (customer_id, product_id, quantity) VALUES ('{customer_id}', '{product_id}','{quantity}')"
            c= con.cursor()
            c.execute(query)
            con.commit()
            print(f"Product ID {product_id} added to the cart for Customer ID {customer_id}. Quantity: {quantity}")
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            con.close()
        
    def removefromcart(self,customer_id,product_id,):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="ecommerce",port="3306",auth_plugin='mysql_native_password')
        try:
            query = f"DELETE FROM cart WHERE customer_id ={customer_id} AND product_id = {product_id}"
            c= con.cursor()
            c.execute(query)
            con.commit()
            if c.rowcount > 0:
                print(f"Product ID {product_id} removed from the cart for Customer ID {customer_id}.")
            else:
                print(f"No product found in the cart for Customer ID {customer_id} with Product ID {product_id}. Nothing was removed.")
            return False
        except Exception as e:
            print(e)
            return None
        finally:
            pass
        
    def get_all_from_cart(self,customer_id):
        try:
            con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="ecommerce",
            port="3306",
            auth_plugin='mysql_native_password'
            )
        
            query = f"SELECT product_id, quantity FROM cart WHERE customer_id = {customer_id}"
            c = con.cursor()
            c.execute(query)
            rows = c.fetchall()
            return rows
        
        except mysql.connector.Error as e:
            print("Error:", e)
            return None
        finally:
            if 'con' in locals() and con.is_connected():
                c.close()
                con.close()
                
    def placeOrder(self, customer_id, shipping_address):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="ecommerce",port="3306",auth_plugin='mysql_native_password')
        try:  
            cart_query = "SELECT p.product_id, p.price, c.quantity FROM cart c INNER JOIN products p ON c.product_id = p.product_id WHERE c.customer_id = %s"
            c = con.cursor()
            c.execute(cart_query, (customer_id,))
            cart_products = c.fetchall()

            if not cart_products:
                print("Cart is empty. Cannot place an order.")
                return False  
            total_price = sum(product[1] * product[2] for product in cart_products)
            order_date = datetime.now().strftime("%Y-%m-%d")
            order_query = "INSERT INTO orders (customer_id, order_date, total_price, shipping_address) VALUES (%s, %s, %s, %s)"
            order_values = (customer_id, order_date, total_price, shipping_address)
            c = con.cursor()
            c.execute(order_query, order_values)
            order_id = c.lastrowid

           
            order_items_query = "INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)"
            for product in cart_products:
                product_id = product[0]
                quantity = product[2]
                item_values = (order_id, product_id, quantity)
                c = con.cursor()
                c.execute(order_items_query, item_values)

            
            clear_cart_query = "DELETE FROM cart WHERE customer_id = %s"
            c = con.cursor()
            c.execute(clear_cart_query, (customer_id,))

            con.commit()
            print(f"Total Price: {total_price}")
            return True
        except Exception as e:
            print(f"Error occurred: {e}")
            return False
        finally:
            c.close()
            
    def getordersbycustomers(self,customer_id):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="ecommerce",port="3306",auth_plugin='mysql_native_password')
        try:
            query = f"SELECT order_id,order_date,total_price, shipping_address quantity FROM orders WHERE customer_id = {customer_id}"
            c = con.cursor()
            c.execute(query)
            rows = c.fetchall()
            return rows
        
        except mysql.connector.Error as e:
            print("Error:", e)
            return None
        finally:
            if 'con' in locals() and con.is_connected():
                c.close()
                con.close()
        
        
        
    
                


        
    
        
    
        
            
            
        
                
                
    
                