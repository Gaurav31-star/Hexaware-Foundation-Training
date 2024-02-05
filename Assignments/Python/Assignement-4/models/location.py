from db_connection.db_adapter import *


class Location:
    def __init__(self, location_id, location_name, address):
        self.connection = get_db_connection()
        self.__location_id = location_id
        self.__location_name = location_name
        self.__address = address

    def get_location_id(self):
        return self.__location_id

    def get_location_name(self):
        return self.__location_name

    def get_address(self):
        return self.__address

    def update_location_details(self, location_name=None, address=None):
        my_cursor = self.connection.cursor()

        if location_name:
            sql = 'UPDATE location SET LocationName = %s WHERE LocationID = %s'
            para = (location_name, self.__location_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('LocationName Updated successfully')

        if address:
            sql = 'UPDATE location SET Address = %s WHERE LocationID = %s'
            para = (address, self.__location_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Address Updated successfully')

        print('Location details updated successfully')

    def info(self):
        print(f"Location ID: {self.get_location_id()}")
        print(f"Location Name: {self.get_location_name()}")
        print(f"Address: {self.get_address()}")
        print("---------------")