class orders:
    def __init__(self, order_id, customer_id, order_date, total_price, shipping_address):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date
        self.total_price = total_price
        self.shipping_address = shipping_address
        
    def get_order_id(self):
        return self.order_id

    def set_order_id(self, order_id):
        self.order_id = order_id

    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_order_date(self):
        return self.order_date

    def set_order_date(self, order_date):
        self.order_date = order_date

    def get_total_price(self):
        return self.total_price

    def set_total_price(self, total_price):
        self.total_price = total_price

    def get_shipping_address(self):
        return self.shipping_address

    def set_shipping_address(self, shipping_address):
        self.shipping_address = shipping_address