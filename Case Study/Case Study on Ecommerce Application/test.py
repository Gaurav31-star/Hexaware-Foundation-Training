import sys
import mysql.connector
import unittest
from Entity import products
from serviceprovider import serviceprovider



class TestEcommerceSystem(unittest.TestCase):
    def setUp(self):
        self.ecommerce = serviceprovider()

    def test_create_product(self):
        name="school bag"
        price=360
        description='its sturdy in nature'
        stockQuantity=100
        created_product =self.ecommerce.create_product(name, price,description,stockQuantity)
        self.assertTrue(created_product)
    
    def test_add_to_cart(self):
        customer_id = 1  
        product_id = 2 
        quantity = 5
        added_to_cart = self.ecommerce.addTocart(customer_id, product_id, quantity)
        self.assertTrue(added_to_cart)

    

    
if __name__ == '__main__':
    unittest.main()
        

        
        
