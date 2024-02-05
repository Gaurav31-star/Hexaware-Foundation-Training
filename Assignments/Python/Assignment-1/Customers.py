from DBconnection import DBConnection
class Customers(DBConnection):
    def __init__(self, customerId, first_name, last_name, email, phone, address):
        self.CustomerID = customerId
        self.FirstName = first_name
        self.LastName = last_name
        self.Email = email
        self.Phone = phone
        self.Address = address

    def get_customer_id(self):
        return self.CustomerID

    def get_firstName(self):
        return self.FirstName

    def get_LastName(self):
        return self.LastName 

    def get_email_address(self):
        return self.Email

    def get_phone_number(self):
        return self.Phone

    def get_address(self):
        return self.Address

    def set_customer_id(self, customerId):
        self.CustomerID = customerId

    def set_firstName(self, first_name):
        self.FirstName = first_name
 
    def set_lastName(self, last_name):
        self.LastName = last_name

    def set_email_address(self, email):
        self.Email = email

    def set_phone_number(self, phone_number):
        self.Phone = phone_number

    def set_address(self, address):
        self.Address = address

    

    def GetCustomerDetails(self):
        print()
        print(f"Customer ID: {self.customerId}")
        print(f"Name: {self.FirstName+ +self.LastName}")
        print(f"Email Address: {self.Email}")
        print(f"Phone Number: {self.Phone}")
        print(f"Address: {self.Address}")
        print()

    def insert_new_customer(self):
        try:
            self.open()
            self.c.execute(f"INSERT INTO Customers (CustomerId,FirstName,LastName,Email, Phone, Address) VALUES ('{self.CustomerID}','{self.FirstName}','{self.LastName}', '{self.Email}', '{self.Phone}', '{self.Address}')")
            self.mydb.commit()
            self.customerId = self.c.lastrowid
            print(f"\nCustomer {self.FirstName} {self.LastName} added to the database with ID: {self.customerId}\n")
        except Exception as e:
            print(e)
        finally:
            self.close()
            return self.customerId  
  

   
 