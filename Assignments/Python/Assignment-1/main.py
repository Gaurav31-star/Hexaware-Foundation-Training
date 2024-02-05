import mysql.connector as connection
from customerrepo import CustomerRepository
from Customers import Customers
from OrderDetails import OrderDetails
from Orders import Orders

class MainModule():
    def main():
        cu = CustomerRepository()
        while True:
            print("\n----------Main Menu----------")
            print("Press-1 to Get Product List")
            print("Press-2 to Place Order")
            print("Press-3 get total no of orders")
            print("Press-4 get customer details")
            print("Press-5 update customer details")
            print("Press-6 update Product details")
            print("Press-7 check product quantity")
            print("Press-8 Final amount of order")
            print("Press-9 Get order details")
            print("Press-0 update order status")
            print("Press-10 cancel order")
            print("Press-11 update quantity in order")
            print("Press-12 update quantity in inventory(add)")
            print("Press-13 update quantity in inventory(remove)")
            print("Press-14 update new quantity for product")
            print("Press-15 check the product avalability")
            print("Press-16 list low stock product")
            print("Press-17 list out of stock product")
            print("Press-18 to Exit")
            ch = int(input())
            if ch == 1:
                cu.show_all_products()   
            elif ch == 2:
                c = int(input('\nEnter Your Customer ID :'))
                cust = cu.getCustomerByID(c)
                if not cust:
                    fn = input('Enter Your FirstName : ')
                    ln = input('Enter Your LastName : ')
                    eml = input('Enter Your Email Address : ')
                    pno = input("Enter Your Phone Number : ")
                    add = input('Enter Your Address : ')
                    customer = Customers(customerId=c,first_name=fn,last_name=ln, email=eml, phone=pno, address=add).insert_new_customer() 
                orderid=input('Enter Orderid: ')
                orderdate=input('Enter today date: ')
                totalamount=input('Enter total amount: ')
                order=Orders(order_id=orderid,customer_id=c,orderDate=orderdate,TotalAmount=totalamount).insert_new_order()
                print("Choose product from the list: ")
                cu.show_all_products()  
                orderdetailid=input('Enter Orderdetailid: ')
                productid=input('Enter Productid: ') 
                quantity=input('Enter the product quantity: ')
                od=OrderDetails(orderdetail_id=orderdetailid,order_id=orderid,product_id=productid,quantity=quantity).insert_new_orderdetails()
                break          
            elif ch == 3:
                c = int(input('\nEnter Your Customer ID :'))
                cu.calculate_total_orders(c)
                break
            elif ch == 4:
                c = int(input('\nEnter Your Customer ID :'))
                cu.getCustomerDetails(c)
                break
            elif ch == 5:
                c = int(input('\nEnter Your Customer ID :'))
                email=str(input('\nEnter new email: '))
                phone=int(input('\nEnter new phone: '))
                address=str(input('\nEnter new address: '))
                cu.updateCustomerInfo(c,email,phone,address)
                break
            elif ch == 6:
                p = int(input('\nEnter Your Product ID :'))
                Description=str(input('\nEnter new description: '))
                price=int(input('\nEnter new price: '))
                cu.updateProductInfo(p,price,Description)
                break
            elif ch == 7:
                p = int(input('\nEnter Your Product ID :'))
                cu.is_product_in_stock(p)
                break
            elif ch==8:
                o=int(input("\nEnter orderid: "))
                cu.calculate_total_amount(o)
                break
            elif ch== 9:
                o=int(input("\nEnter orderid: "))
                cu.get_order_details(o)
                break
            elif ch== 0:
                o=int(input("\nEnter orderid: "))
                status=str(input("\nEnter new statue: "))
                cu.update_order_status(o,status)
                break
            elif ch== 10:
                o=int(input("\nEnter orderid: "))
                cu.cancel_order(o)
                break
            elif ch== 11:
                o=int(input("\nEnter orderdetailid: "))
                q=int(input("\nEnter correct quantity: "))
                cu.update_quantity(o,q)
                break
            elif ch== 12:
                p=int(input("\nEnter productid: "))
                q=int(input("\nEnter updated quantity: "))
                cu.add_to_inventory(p,q)
                break
            elif ch== 13:
                p=int(input("\nEnter productid: "))
                q=int(input("\nEnter updated quantity: "))
                cu.remove_from_inventory(p,q)
                break
            elif ch== 14:
                p=int(input("\nEnter productid: "))
                q=int(input("\nEnter new quantity: "))
                cu.update_stock_quantity(p,q)
                break
            elif ch== 15:
                p=int(input("\nEnter productid: "))
                q=int(input("\nEnter quantity you want to check: "))
                cu.is_product_available(p,q)
                break
            elif ch== 16:
                q=int(input("\nEnter quantity you want to check: "))
                cu.list_low_stock_products(q)
                break
            elif ch== 17:
                cu.list_out_of_stock_products()
                break
            elif ch == 18:
                print("\nThank You\n")
                break            
            else:
                print('\nInvalid Choice!!\nPlease Try Again...\n')



if __name__ == "__main__":
    MainModule.main()