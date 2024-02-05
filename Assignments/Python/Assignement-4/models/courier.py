import random

from custom_exceptions.custom_exception import CourierNotFound
from db_connection.db_adapter import *


class Courier:
    def __init__(self, courier_id, sender_name, sender_address, receiver_name, receiver_address, weight, status,
                 tracking_number, delivery_date):
        self.connection = get_db_connection()
        self.__courier_id = courier_id
        self.__sender_name = sender_name
        self.__sender_address = sender_address
        self.__receiver_name = receiver_name
        self.__receiver_address = receiver_address
        self.__weight = weight
        self.__status = status
        self.__tracking_number = tracking_number
        self.__delivery_date = delivery_date

    def get_courier_id(self):
        return self.__courier_id

    def get_sender_name(self):
        return self.__sender_name

    def get_sender_address(self):
        return self.__sender_address

    def get_receiver_name(self):
        return self.__receiver_name

    def get_receiver_address(self):
        return self.__receiver_address

    def get_weight(self):
        return self.__weight

    def get_status(self):
        return self.__status

    def get_tracking_number(self):
        return self.__tracking_number

    def get_delivery_date(self):
        return self.__delivery_date

    def update_courier_details(self, sender_name=None, sender_address=None, receiver_name=None, receiver_address=None,
                               weight=None, status=None, tracking_number=None, delivery_date=None):
        my_cursor = self.connection.cursor()

        if sender_name:
            sql = 'UPDATE courier SET SenderName = %s WHERE CourierID = %s'
            para = (sender_name, self.__courier_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('SenderName Updated successfully')

        if sender_address:
            sql = 'UPDATE courier SET SenderAddress = %s WHERE CourierID = %s'
            para = (sender_address, self.__courier_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('SenderAddress Updated successfully')

        if receiver_name:
            sql = 'UPDATE courier SET ReceiverName = %s WHERE CourierID = %s'
            para = (receiver_name, self.__courier_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('ReceiverName Updated successfully')

        if receiver_address:
            sql = 'UPDATE courier SET ReceiverAddress = %s WHERE CourierID = %s'
            para = (receiver_address, self.__courier_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('ReceiverAddress Updated successfully')

        if weight:
            sql = 'UPDATE courier SET Weight = %s WHERE CourierID = %s'
            para = (weight, self.__courier_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Weight Updated successfully')

        if status:
            sql = 'UPDATE courier SET Status = %s WHERE CourierID = %s'
            para = (status, self.__courier_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Status Updated successfully')

        if tracking_number:
            sql = 'UPDATE courier SET TrackingNumber = %s WHERE CourierID = %s'
            para = (tracking_number, self.__courier_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('TrackingNumber Updated successfully')

        if delivery_date:
            sql = 'UPDATE courier SET DeliveryDate = %s WHERE CourierID = %s'
            para = (delivery_date, self.__courier_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('DeliveryDate Updated successfully')

        print('Courier details updated successfully')

    def info(self):
        print(f"Courier ID: {self.get_courier_id()}")
        print(f"Sender Name: {self.get_sender_name()}")
        print(f"Sender Address: {self.get_sender_address()}")
        print(f"Receiver Name: {self.get_receiver_name()}")
        print(f"Receiver Address: {self.get_receiver_address()}")
        print(f"Weight: {self.get_weight()}")
        print(f"Status: {self.get_status()}")
        print(f"Tracking Number: {self.get_tracking_number()}")
        print(f"Delivery Date: {self.get_delivery_date()}")
        print("---------------")

    def place_courier(self, sender_name, sender_address, receiver_name, receiver_address, weight, status,
                      tracking_number, delivery_date):
        connection = get_db_connection()
        my_cursor = self.connection.cursor()

        try:
            # Assuming that the CourierID is auto-incremented in the database
            sql = '''
                    INSERT INTO courier (CourierID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                '''
            para = (
                get_ids('courier', 'CourierID'), sender_name, sender_address, receiver_name, receiver_address, weight,
                status, tracking_number,
                delivery_date)
            my_cursor.execute(sql, para)
            connection.commit()
            print('Courier placed successfully.')
        except Exception as e:
            print(f'Error placing courier: {e}')
        finally:
            connection.close()

    def cancel_courier(self, courierID):
        my_cursor = self.connection.cursor()
        courier_exists = get_cnts('courier', 'CourierID', courierID)

        try:
            if courier_exists > 0:
                sql = '''DELETE FROM Courier WHERE CourierID = %s'''
                para = (courier_exists,)
                my_cursor.execute(sql, para)
                self.connection.commit()
                print('Courier Order deleted successfully')
            else:
                raise CourierNotFound('Invalid Courier ID')
        except CourierNotFound as c:
            print(c)
        except Exception as e:
            print('An error occurred', e)

    @classmethod
    def generate_tracking_number(cls):
        random_number = random.randint(100000, 999999)
        tracking_number = f"TN{random_number}"
        return tracking_number