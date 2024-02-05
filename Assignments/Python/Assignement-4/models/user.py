from db_connection.db_adapter import *

class User:
    def __init__(self, user_id, name, email, password, contact_number, address):
        self.connection = get_db_connection()
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__password = password
        self.__contact_number = contact_number
        self.__address = address

    def get_user_id(self): return self.__user_id
    def get_user_name(self): return self.__name
    def get_user_email(self): return self.__email
    def get_user_password(self): return self.__password
    def get_user_contact_number(self): return self.__contact_number
    def get_user_address(self): return self.__address

    def update_user_details(self, name=None, email=None, password=None, contact_number=None, address=None):
        my_cursor = self.connection.cursor()

        if name:
            sql = 'UPDATE user SET name = %s WHERE userID = %s'
            para = (name, self.__user_id)
            my_cursor.execute(sql, para)
            self.connection.connect()
            print('Name Updated successfully')

        if email:
            sql = 'UPDATE user SET email = %s WHERE userID = %s'
            para = (email, self.__user_id)
            my_cursor.execute(sql, para)
            self.connection.connect()
            print('email Updated successfully')

        if password:
            sql = 'UPDATE user SET password = %s WHERE userID = %s'
            para = (password, self.__user_id)
            my_cursor.execute(sql, para)
            self.connection.connect()
            print('password Updated successfully')

        if contact_number:
            sql = 'UPDATE user SET ContactNumber = %s WHERE userID = %s'
            para = (contact_number, self.__user_id)
            my_cursor.execute(sql, para)
            self.connection.connect()
            print('contact_number Updated successfully')

        if address:
            sql = 'UPDATE user SET address = %s WHERE userID = %s'
            para = (address, self.__user_id)
            my_cursor.execute(sql, para)
            self.connection.connect()
            print('address Updated successfully')

        print('User details updated successfully')

    def info(self):
        print(f"User ID: {self.get_user_id()}")
        print(f"Name: {self.get_user_name()}")
        print(f"Email: {self.get_user_email()}")
        print(f"Contact Number: {self.get_user_contact_number()}")
        print(f"Address: {self.get_user_address()}")
        print("---------------")