from db_connection.db_adapter import *  # Import your database adapter module

class CourierService:
    # ... (previous code remains unchanged)

    @staticmethod
    def add_courier_services(service_id, service_name, cost, employee_id):
        connection = get_db_connection()
        my_cursor = connection.cursor()
        # print(service_id, service_name, cost, employee_id)
        try:
            if not CourierService.is_employee_admin(employee_id):
                raise PermissionError("Only admins can add courier services.")

            # Add courier service to the database
            sql = '''
                INSERT INTO courierservices (ServiceID, ServiceName, Cost)
                VALUES (%s, %s, %s)
            '''
            para = (service_id, service_name, cost)
            my_cursor.execute(sql, para)
            connection.commit()
            print('Courier service added successfully.')
        except PermissionError as e:
            print(f'Error: {e}')
        except Exception as e:
            print(f'Error adding courier service: {e}')
        finally:
            connection.close()

    @staticmethod
    def is_employee_admin(employee_id):
        admin_counts = get_counts('employee', 'employeeID', 'role', employee_id, 'Admin')
        print(admin_counts)
        return admin_counts > 0

# Example usage:
CourierService.add_courier_services(
    service_id=get_ids('courierservices', 'ServiceID'),
    service_name="Express Delivery",
    cost=10.99,
    employee_id="2"
)