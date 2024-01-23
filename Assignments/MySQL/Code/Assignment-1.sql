create database techshop;
use techshop;

create table Customers(CustomerID int,FirstName text,LastName text,Email text,Phone int,Address text, primary key(CustomerID));
desc Customers;

create table Products(ProductID int, ProductName text, Description text,Price int,primary key(ProductID));
desc Products;

create table Orders(OrderID int, CustomerID int, Orderdate date,TotalAmount int,primary key(OrderID),foreign key(CustomerID) references customers(CustomerID));
desc Orders;

create table OrderDetails(OrderDetailID int, OrderID int, ProductID int,Quantity int,primary key(OrderDetailID),foreign key(OrderID) references Orders(OrderID),foreign key(ProductID) references Products(ProductID));
desc OrderDetails;

create table Inventory(InventoryID int, ProductID int, QuantityInStock int, LastStockUpdate int,primary key(InventoryID),foreign key(ProductID) references Products(ProductID));
desc Inventory;

insert into Customers values(1,"Alex","Johnson","alex@gmail.com",1234567890,"new mexico");
insert into Customers values(2,"Jordan","D","jordan@gmail.com",1234565890,"LA"),(3,"Kylie","Jenner","kylie@gmail.com",1234565890,"California"),
(4,"Taylor","Swift","taylor@gmail.com",1234565890,"NewYork"),(5,"Lionnel","Messi","messi@gmail.com",1234565890,"Miami"),
(6,"Enrique","Iglesias","enrique@gmail.com",1234565890,"Miami"),(7,"Marshall","Matthers","eminem@yahoo.com",1234565890,"LA"),
(8,"John","Mayer","john@yahoo.com",1234565890,"Charlotte"),(9,"Jay","Z","jayZ@gmail.com",1234565890,"LA"),
(10,"Selena","Gomez","selena@gmail.com",1234565890,"California");
select * from customers;

insert into products values(1, 'Smart TV', '50-inch Smart TV with HDR', 1000),(2, 'Watch', 'a digitl watch with call features', 1001),
(3, 'Digital Camera', '28MP DSLR Camera', 1003),(4, 'Soundbar', 'Sound Soundbar with Subwoofer', 1004),
(5, 'Gaming Console', 'Next-gen gaming console', 1005),('6', 'Wireless Headphones', 'Over-ear Bluetooth headphones', 1006),
(7, 'Laptop', '15.6-inch Full HD Laptop with Intel Core i9 processor', 1007),(8, 'Wireless Router', 'Dual-band router', 1008),
(9, 'Fitness Tracker', 'Water-resistant fitness tracker', 1009), (10, 'Virtual Reality Headset', 'Immersive VR headset', 1010);
select * from products;

insert into orders values(1, 7, '2023-11-15', 60999),(2, 3, '2023-10-28', 42999),(3, 2, '2023-07-10', 15999),
(4, 5, '2023-04-05', 53999),(5, 8, '2023-12-22', 23999),(6, 10, '2023-01-17', 30999),
(7, 6, '2023-11-03', 8000),(8, 1, '2023-04-12', 12999),(9, 4, '2023-01-28', 41999),
(10, 9, '2023-06-09', 15999);
select * from orders;

insert into OrderDetails values(1, 2, 1, 1),(2, 4, 3, 2), (3, 8, 5, 3), (4, 6, 7, 1),
(5, 1, 10, 1),(6, 2, 2, 2),(7, 10, 8, 1),(8, 2, 6, 1),(9, 1, 4, 2),(10, 7, 9, 1);
select * from orderdetails;
truncate table inventory;
insert into Inventory values(11, 1, 5, 4),(12, 2, 3, 2),(13, 3, 8, 7),(14, 4, 5, 10),(15, 5, 20, 5),
(16, 6, 2, 10),(17, 7, 25, 22),(18, 8, 4, 4),(19, 9, 10, 5),(20, 10, 20, 18);
select * from inventory;

/* 1. Write an SQL query to retrieve the names and emails of all customers.*/
select concat(firstName," ",LastName) as full_name, Email from customers;
/* 2. Write an SQL query to list all orders with their order dates and corresponding customer names.*/
select OrderID, OrderDate, CONCAT(FirstName, ' ', LastName) as full_name
from orders O, customers C
where O.CustomerID = C.CustomerID;
/*3. Write an SQL query to insert a new customer record into the "Customers" table. 
Include customer information such as name, email, and address.*/
insert into customers values(11,"Jack","Sparrow","jack@yahoo.com",1236547890,"Tortuga");
select * from customers;

/*4. Write an SQL query to update the prices of all electronic gadgets in the "Products" table
 by increasing them by 10%.*/
update Products set Price = Price * 1.1 where ProductID > 0;
select * from products;

/*5 Write an SQL query to delete a specific order and its associated order details from the "Orders" and "OrderDetails" tables.
 Allow users to input the order ID as a parameter.*/
 delete from orders where OrderID = 10;
 
 /*6. Write an SQL query to insert a new order into the "Orders" table.
 Include the customer ID, order date, and any other necessary information.*/
 insert into orders values(20, 7, '2023-06-09', 68999);
 select * from orders;
 
 /*7. Write an SQL query to update the contact information (e.g., email and address) of a specific customer in the "Customers" table.
 Allow users to input the customer ID and new contact information.*/
update Customers set Email = "EminemM@gmail.com", Address = "NewYork" where CustomerID = 7;
select * from customers;

/*8 Write an SQL query to recalculate and update the total cost of each order in the "Orders" table 
based on the prices and quantities in the "OrderDetails" table.*/

/*9. Write an SQL query to delete all orders and their associated order details for a specific customer from the "Orders" and "OrderDetails" tables.
 Allow users to input the customer ID as a parameter.*/
set @customerID = 3;
delete from orderdetails where OrderID in (select OrderID from orders where CustomerID = @customerid);
delete from orders where CustomerID = @customerid;
select * from orders;
select * from orderdetails;

/*10. Write an SQL query to insert a new electronic gadget product into the "Products" table, 
including product name, category, price, and any other relevant details.*/
insert into products values (11, 'Sony Bluetooth Speaker', 'Experience immersive sound', 5499);
select * from products;

/*11. Write an SQL query to update the status of a specific order in the "Orders" table (e.g., from "Pending" to "Shipped").
 Allow users to input the order ID and the new status.*/
alter table orders add OrderStatus VARCHAR(20) DEFAULT 'Pending';
update orders set OrderStatus = 'Pending' where OrderStatus is null;
set @oidup = '7';
update orders set OrderStatus = 'Shipped' where OrderID = @oidup;
select * from orders;

/* 12. Write an SQL query to calculate and update the number of orders placed by each customer 
in the "Customers" table based on the data in the "Orders" table.*/
alter table customers Add NumberOfOrders int;
update customers set NumberOfOrders =
   (select COUNT(*) from orders where orders.CustomerID = customers.CustomerID);

/*JOIN*/
/*1. Write an SQL query to retrieve a list of all orders along with customer information
 (e.g., customer name) for each order.*/
SELECT Orders.OrderID, Orders.Orderdate, Orders.TotalAmount, Customers.FirstName, Customers.LastName
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

/*2*/
/*Write an SQL query to find the total revenue generated by each electronic gadget product.Include the product name and the total revenue.*/
SELECT p.ProductName, SUM(od.Quantity * o.TotalAmount) AS TotalRevenue
FROM Products p
JOIN OrderDetails od ON p.ProductID = od.ProductID
JOIN Orders o ON od.OrderID = o.OrderID
WHERE p.Description = 'Electronic' 
GROUP BY p.ProductName;

/*3*/
/*Write an SQL query to list all customers who have made at least one purchase. Include their names and contact information.*/
SELECT DISTINCT c.FirstName, c.LastName, c.Email, c.Phone, c.Address
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID;

/*4*/
/*Write an SQL query to find the most popular electronic gadget, which is the one with the highest total quantity ordered.
 Include the product name and the total quantity ordered.*/
SELECT p.ProductName, SUM(od.Quantity) AS TotalQuantityOrdered
FROM Products p
JOIN OrderDetails od ON p.ProductID = od.ProductID
WHERE p.ProductName = 'TV'
GROUP BY p.ProductName
ORDER BY TotalQuantityOrdered DESC
LIMIT 1;

/*5*/
/*Write an SQL query to retrieve a list of electronic gadgets along with their corresponding categories.*/
SELECT ProductName, Description
FROM Products
WHERE Description = 'Electronic'; 

/*6*/
/*Write an SQL query to calculate the average order value for each customer. Include the customer's name and their average order value.*/
SELECT c.FirstName, c.LastName, AVG(o.TotalAmount) AS AverageOrderValue
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.FirstName, c.LastName;

/*7*/
/*7. Write an SQL query to find the order with the highest total revenue. Include the order ID,customer information, and the total revenue.*/
SELECT o.OrderID, c.FirstName, c.LastName, c.Email, c.Phone, c.Address, SUM(od.Quantity * p.Price) AS TotalRevenue
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
GROUP BY o.OrderID, c.FirstName, c.LastName, c.Email, c.Phone, c.Address
ORDER BY TotalRevenue DESC
LIMIT 1;

/*8*/
/*Write an SQL query to list electronic gadgets and the number of times each product has been ordered.*/
SELECT p.ProductName, COUNT(od.ProductID) AS TimesOrdered
FROM Products p
LEFT JOIN OrderDetails od ON p.ProductID = od.ProductID
LEFT JOIN Orders o ON od.OrderID = o.OrderID
WHERE p.ProductName = 'Smart TV' 
GROUP BY p.ProductName;

/*9*/
/*Write an SQL query to find customers who have purchased a specific electronic gadget product.
Allow users to input the product name as a parameter.*/
SET @productName = 'Smart TV'; 
SELECT DISTINCT c.FirstName, c.LastName, c.Email, c.Phone, c.Address
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE p.ProductName = @productName;

/*10*/
/*Write an SQL query to calculate the total revenue generated by all orders placed within a specific time period.
 Allow users to input the start and end dates as parameters.*/
SET @startDate = '2023-05-01'; 
SET @endDate = '2023-12-31'; 
SELECT SUM(o.TotalAmount) AS TotalRevenue
FROM Orders o
WHERE o.Orderdate BETWEEN @startDate AND @endDate;

/*sub-query*/
/*1*/
/*Write an SQL query to find out which customers have not placed any orders.*/
SELECT c.CustomerID, c.FirstName, c.LastName, c.Email, c.Phone, c.Address
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
WHERE o.OrderID IS NULL;

/*2*/
/*Write an SQL query to find the total number of products available for sale.*/
SELECT COUNT(*) AS TotalProductsAvailable
FROM Products;

/*3*/
/*Write an SQL query to calculate the total revenue generated by TechShop.*/
SELECT SUM(TotalAmount) AS TotalRevenue
FROM ORDERS;

/*4*/
/*Write an SQL query to calculate the average quantity ordered for products in a specific category.
 Allow users to input the category name as a parameter*/
 SET @categoryName = 'Electronics';
SELECT AVG(od.Quantity) AS AverageQuantityOrdered
FROM OrderDetails od
JOIN Products p ON od.ProductID = p.ProductID
WHERE p.Category = @categoryName;

/*5*/
/*Write an SQL query to calculate the total revenue generated by a specific customer. Allow users to input the customer ID as a parameter.*/
SET @cuid = 5;
SELECT SUM(TotalAmount) AS RevenueOfSelectedCustomer
FROM ORDERS
WHERE CustomerID = @cuid;

/*6*/
/*Write an SQL query to find the customers who have placed the most orders. List their names 
and the number of orders they've placed*/
SELECT c.FirstName, c.LastName, COUNT(o.OrderID) AS NumberOfOrdersPlaced
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.FirstName, c.LastName
ORDER BY NumberOfOrdersPlaced DESC
LIMIT 1;

/*7*/
/*Write an SQL query to find the most popular product category, which is the one with the highest 
total quantity ordered across all orders*/
SELECT p.Description, SUM(od.Quantity) AS TotalQuantityOrdered
FROM Products p
JOIN OrderDetails od ON p.ProductID = od.ProductID
GROUP BY p.Description
ORDER BY TotalQuantityOrdered DESC
LIMIT 1;

/*8*/
/*Write an SQL query to find the customer who has spent the most money (highest total revenue) 
on electronic gadgets. List their name and total spending*/
SELECT c.FirstName, c.LastName, SUM(o.TotalAmount) AS TotalSpending
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE p.Description = 'Sound Soundbar with Subwoofer'
GROUP BY c.FirstName, c.LastName
ORDER BY TotalSpending DESC
LIMIT 1;

/*9*/
/*Write an SQL query to calculate the average order value (total revenue divided by the number of orders) for all customers*/
SELECT AVG(TotalAmount) AS AverageOrderValue
FROM (
    SELECT SUM(TotalAmount) AS TotalAmount
    FROM Orders
    GROUP BY CustomerID
) AS CustomerOrders;

/*10*/
/*Write an SQL query to find the total number of orders placed by each customer and list their names along with the order count*/
SELECT c.FirstName, c.LastName, COUNT(o.OrderID) AS OrderCount
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.FirstName, c.LastName;









 




















