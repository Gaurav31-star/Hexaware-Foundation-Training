from db_connection.db_adapter import *


class CourierService:
    def __init__(self, service_id, service_name, cost):
        self.connection = get_db_connection()
        self.__service_id = service_id
        self.__service_name = service_name
        self.__cost = cost

    def get_service_id(self):
        return self.__service_id

    def get_service_name(self):
        return self.__service_name

    def get_cost(self):
        return self.__cost

    def update_courier_service_details(self, service_name=None, cost=None):
        my_cursor = self.connection.cursor()

        if service_name:
            sql = 'UPDATE courierservices SET ServiceName = %s WHERE ServiceID = %s'
            para = (service_name, self.__service_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('ServiceName Updated successfully')

        if cost:
            sql = 'UPDATE courierservices SET Cost = %s WHERE ServiceID = %s'
            para = (cost, self.__service_id)
            my_cursor.execute(sql, para)
            self.connection.commit()
            print('Cost Updated successfully')

        print('Courier service details updated successfully')

    def info(self):
        print(f"Service ID: {self.get_service_id()}")
        print(f"Service Name: {self.get_service_name()}")
        print(f"Cost: {self.get_cost()}")
        print("---------------")