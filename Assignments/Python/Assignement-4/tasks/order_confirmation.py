def generate_order_confirmation_email(customer_name, order_number, delivery_address, expected_delivery_date):
    email_body = (f"Dear {customer_name},\n\nOrder Number: "
                  f"{order_number}\nDelivery Address: {delivery_address}\nExpected Delivery Date: "
                  f"{expected_delivery_date}\n\nThank you for choosing our courier service!")

    return email_body


# Example usage
customer_name = "John Doe"
order_number = "123456"
delivery_address = "123 Main St, Example City, NY 12345"
expected_delivery_date = "2023-01-01"

order_confirmation_email = generate_order_confirmation_email(customer_name, order_number, delivery_address,
                                                             expected_delivery_date)
print("Order Confirmation Email:\n", order_confirmation_email)