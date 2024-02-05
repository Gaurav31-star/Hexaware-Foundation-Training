from models.courier import Courier
from services.CourierServiceManager import CourierService
from datetime import datetime

class CourierSystemMenu:
    def __init__(self):
        self.courier_service = CourierService()

    def display_menu(self):
        while True:
            print("\nCourier System Menu:")
            print("1. Place Courier Order")
            print("2. Check Order Status")
            print("3. Cancel Courier Order")
            print("4. Get Assigned Orders (Courier Staff)")
            print("5. Add Courier Service (Admin)")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.place_courier_order()
            elif choice == "2":
                self.check_order_status()
            elif choice == "3":
                self.cancel_courier_order()
            elif choice == "4":
                self.get_assigned_orders()
            elif choice == "5":
                self.add_courier_service()
            elif choice == "6":
                print("Exiting Courier System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def place_courier_order(self):
        # Implement the logic to gather details from the user and place a courier order
        # Example:
        sender_name = input("Enter sender name: ")
        sender_address = input("Enter sender address: ")
        receiver_name = input("Enter receiver name: ")
        receiver_address = input("Enter receiver address: ")
        weight = float(input("Enter weight: "))
        status = input("Yet to Transit")
        tracking_number = input(Courier.generate_tracking_number())
        delivery_date = input("Enter delivery date (YYYY-MM-DD): ")

        courier_order = Courier(sender_name, sender_address, receiver_name, receiver_address, weight,status,tracking_number,delivery_date)
        courier_order.status = status
        courier_order.tracking_number = tracking_number
        courier_order.delivery_date = datetime.strptime(delivery_date, "%Y-%m-%d").date()

        print(f"Courier order placed successfully. Tracking Number: {tracking_number}")

    def check_order_status(self):
        tracking_number = input("Enter tracking number: ")
        # Implement logic to retrieve and display the order status based on the tracking number
        # Example:
        order_status = "In Transit"  # Replace with your actual logic
        print(f"Order Status: {order_status}")

    def cancel_courier_order(self):
        tracking_number = input("Enter tracking number to cancel: ")
        # Implement logic to cancel the courier order based on the tracking number
        # Example:
        is_canceled = True  # Replace with your actual logic
        if is_canceled:
            print("Order canceled successfully.")
        else:
            print("Error canceling order.")

    def get_assigned_orders(self):
        courier_staff_id = input("Enter courier staff ID: ")
        # Implement logic to retrieve and display assigned orders for the courier staff
        # Example:
        assigned_orders = ["123456", "789012"]  # Replace with your actual logic
        print(f"Assigned Orders: {assigned_orders}")

    def add_courier_service(self):
        employee_id = input("Enter admin employee ID: ")
        if self.courier_service.is_employee_admin(employee_id):
            # Only allow adding courier service if the employee is an admin
            service_id = int(input("Enter service ID: "))
            service_name = input("Enter service name: ")
            cost = float(input("Enter cost: "))
            self.courier_service.add_courier_services(service_id, service_name, cost, employee_id)
        else:
            print("Error: Only admins can add courier services.")

if __name__ == "__main__":
    menu = CourierSystemMenu()
    menu.display_menu()