from db_connection.db_adapter import *

class Employee:
    def __init__(self, employee_id, name, email, contact_number, role, salary):
        self.connection = get_db_connection()
        self.__employee_id = employee_id
        self.__name = name
        self.__email = email
        self.__contact_number = contact_number
        self.__role = role
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def get_employee_name(self):
        return self.__name

    def get_employee_email(self):
        return self.__email

    def get_employee_contact_number(self):
        return self.__contact_number

    def get_employee_role(self):
        return self.__role

    def get_employee_salary(self):
        return self.__salary

    def update_employee_details(self, name=None, email=None, contact_number=None, role=None, salary=None):
        my_cursor = self.connection.cursor()

        if name:
            sql = 'UPDATE employee SET Name = %s WHERE EmployeeID = %s'
            para = (name, self.__employee_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Name Updated successfully')

        if email:
            sql = 'UPDATE employee SET Email = %s WHERE EmployeeID = %s'
            para = (email, self.__employee_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Email Updated successfully')

        if contact_number:
            sql = 'UPDATE employee SET ContactNumber = %s WHERE EmployeeID = %s'
            para = (contact_number, self.__employee_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('ContactNumber Updated successfully')

        if role:
            sql = 'UPDATE employee SET Role = %s WHERE EmployeeID = %s'
            para = (role, self.__employee_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Role Updated successfully')

        if salary:
            sql = 'UPDATE employee SET Salary = %s WHERE EmployeeID = %s'
            para = (salary, self.__employee_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Salary Updated successfully')

        print('Employee details updated successfully')

    def info(self):
        print(f"Employee ID: {self.get_employee_id()}")
        print(f"Name: {self.get_employee_name()}")
        print(f"Email: {self.get_employee_email()}")
        print(f"Contact Number: {self.get_employee_contact_number()}")
        print(f"Role: {self.get_employee_role()}")
        print(f"Salary: {self.get_employee_salary()}")
        print("---------------")