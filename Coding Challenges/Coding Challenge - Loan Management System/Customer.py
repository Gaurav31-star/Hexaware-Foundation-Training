class Customer():
    def __init__(self, customer_id=None, name=None, email_address=None, phone_number=None, address=None, credit_score=None):
        self.customer_id = customer_id
        self.name = name
        self.email_address = email_address
        self.phone_number = phone_number
        self.address = address
        self.credit_score = credit_score

    def get_customer_id(self):
        return self.customer_id

    def get_name(self):
        return self.name

    def get_email_address(self):
        return self.email_address

    def get_phone_number(self):
        return self.phone_number

    def get_address(self):
        return self.address

    def get_credit_score(self):
        return self.credit_score

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_name(self, name):
        self.name = name

    def set_email_address(self, email_address):
        self.email_address = email_address

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_address(self, address):
        self.address = address

    def set_credit_score(self, credit_score):
        self.credit_score = credit_score

    def display_customer_details(self):
        print()
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Email Address: {self.email_address}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Address: {self.address}")
        print(f"Credit Score: {self.credit_score}")
        print()

    def insert_new_customer(self):
        try:
            self.open()
            self.c.execute(f"INSERT INTO Customer (name, email_address, phone_number, address, credit_score) VALUES ('{self.name}', '{self.email_address}', '{self.phone_number}', '{self.address}', {self.credit_score})")
            self.mydb.commit()
            self.customer_id = self.c.lastrowid
            print(f"\nCustomer '{self.name}' added to the database with ID: {self.customer_id}\n")
        except Exception as e:
            print(e)
        finally:
            self.close()
            return self.customer_id
