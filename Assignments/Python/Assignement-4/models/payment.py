from db_connection.db_adapter import *

class Payment:
    def __init__(self, payment_id, courier_id, location_id, amount, payment_date):
        self.connection = get_db_connection()
        self.__payment_id = payment_id
        self.__courier_id = courier_id
        self.__location_id = location_id
        self.__amount = amount
        self.__payment_date = payment_date

    def get_payment_id(self):
        return self.__payment_id

    def get_courier_id(self):
        return self.__courier_id

    def get_location_id(self):
        return self.__location_id

    def get_amount(self):
        return self.__amount

    def get_payment_date(self):
        return self.__payment_date

    def update_payment_details(self, courier_id=None, location_id=None, amount=None, payment_date=None):
        my_cursor = self.connection.cursor()

        if courier_id:
            sql = 'UPDATE payment SET CourierID = %s WHERE PaymentID = %s'
            para = (courier_id, self.__payment_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('CourierID Updated successfully')

        if location_id:
            sql = 'UPDATE payment SET LocationID = %s WHERE PaymentID = %s'
            para = (location_id, self.__payment_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('LocationID Updated successfully')

        if amount:
            sql = 'UPDATE payment SET Amount = %s WHERE PaymentID = %s'
            para = (amount, self.__payment_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Amount Updated successfully')

        if payment_date:
            sql = 'UPDATE payment SET PaymentDate = %s WHERE PaymentID = %s'
            para = (payment_date, self.__payment_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('PaymentDate Updated successfully')

        print('Payment details updated successfully')

    def info(self):
        print(f"Payment ID: {self.get_payment_id()}")
        print(f"Courier ID: {self.get_courier_id()}")
        print(f"Location ID: {self.get_location_id()}")
        print(f"Amount: {self.get_amount()}")
        print(f"Payment Date: {self.get_payment_date()}")
        print("---------------")