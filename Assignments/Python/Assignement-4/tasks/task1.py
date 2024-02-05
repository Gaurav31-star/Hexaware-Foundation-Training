def check_order_delivery_status(order_status):
    if order_status == "Delivered":
        print("The order has been delivered.")
    elif order_status == "Processing":
        print("The order is still in processing.")
    elif order_status == "Cancelled":
        print("The order has been cancelled.")
    else:
        print("Invalid order status.")


def categorize_parcel_by_weight(parcel_weight):
    if 0 < parcel_weight <= 3:
        print("Light parcel")
    elif 3 < parcel_weight <= 10:
        print("Medium parcel")
    elif parcel_weight > 10:
        print("Heavy parcel")
    else:
        print("Invalid parcel weight")


def user_authentication(username, password, user_type):
    if user_type == 'employee' and username == 'admin' and password == 'admin123':
        print("Employee login successful.")
    elif user_type == 'customer' and username == 'customer' and password == 'password123':
        print("Customer login successful.")
    else:
        print("Invalid username or password.")


def assign_couriers_to_shipments(shipments):
    for shipment in shipments:
        print(f"Courier assigned for shipment {shipment}")


shipments_list = [1, 2, 3]
assign_couriers_to_shipments(shipments_list)

username_input = input("Enter username: ")
password_input = input("Enter password: ")
user_type_input = input("Enter user type (employee/customer): ")
user_authentication(username_input, password_input, user_type_input)

parcel_weight = 7
categorize_parcel_by_weight(parcel_weight)

order_status = "Delivered"
check_order_delivery_status(order_status)