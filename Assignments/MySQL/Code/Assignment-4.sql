show databases;
create database couriermanagementsystem;
show databases;
use couriermanagementsystem;
/*task 1*/
create table Usertable(userid int primary key,name varchar(255),email varchar(255), unique(email),password
varchar(255),contactnumber varchar(20),address text);
desc usertable;

create table courier(courierid int primary key, SenderName VARCHAR(255), SenderAddress TEXT,
ReceiverName VARCHAR(255), ReceiverAddress TEXT, Weight DECIMAL(5, 2), Status VARCHAR(50), 
TrackingNumber VARCHAR(20) UNIQUE, DeliveryDate DATE); 
desc courier;

create table CourierServices (ServiceID INT PRIMARY KEY, ServiceName VARCHAR(100), Cost DECIMAL(8, 2)); 
desc courierservices;

create table Employee(EmployeeID INT PRIMARY KEY, Name VARCHAR(255), Email VARCHAR(255) UNIQUE, 
ContactNumber VARCHAR(20), Role VARCHAR(50), Salary DECIMAL(10, 2)); 
desc employee;

create table Location(LocationID INT PRIMARY KEY, LocationName VARCHAR(100), Address TEXT);
desc location; 

create table Payment(PaymentID INT PRIMARY KEY, CourierID INT, LocationId INT, Amount DECIMAL(10, 2), 
PaymentDate DATE, FOREIGN KEY (CourierID) REFERENCES Courier(CourierID), 
FOREIGN KEY (LocationID) REFERENCES Location(LocationID));
desc payment;

INSERT INTO UserTable VALUES 
(1, 'John Doe', 'johndoe@example.com', 'password123', '1234567890', '123 Main Street'),
(2, 'Jane Smith', 'janesmith@example.com', 'securepass', '9876543210', '456 Elm Street'),
(3, 'Alice Johnson', 'alice@example.com', 'pass1234', '5555555555', '789 Oak Avenue'),
(4, 'Bob Brown', 'bob@example.com', 'qwerty', '7778889999', '101 Pine Road'),
(5, 'Eva Garcia', 'eva@example.com', 'evapass', '4443332222', '321 Cedar Lane');
select * from usertable;

INSERT INTO Courier VALUES 
(1, 1, 2, '123 Main Street', '456 Elm Street', 2.5, 'Delivered', 'TRK123', '2023-01-15'),
(2, 3, 4, '789 Oak Avenue', '101 Pine Road', 1.8, 'Pending', 'TRK456', NULL),
(3, 4, 1, '101 Pine Road', '123 Main Street', 3.0, 'In Transit', 'TRK789', NULL),
(4, 2, 5, '456 Elm Street', '321 Cedar Lane', 4.2, 'Pending', 'TRK987', NULL),
(5, 5, 3, '321 Cedar Lane', '789 Oak Avenue', 2.7, 'Delivered', 'TRK654', '2023-02-05');
select * from courier;

INSERT INTO CourierServices VALUES 
(1, 'Standard', 10.00),
(2, 'Express', 20.00),
(3, 'Overnight', 30.00),
(4, 'International', 50.00),
(5, 'Same-day', 40.00);
select * from courierservices;

INSERT INTO Employee VALUES 
(1, 'Mark Johnson', 'mark@example.com', '1112223333', 'Admin', 60000.00),
(2, 'Sarah Lee', 'sarah@example.com', '9998887777', 'Manager', 50000.00),
(3, 'Michael Davis', 'michael@example.com', '3334445555', 'Staff', 40000.00),
(4, 'Emily Wilson', 'emily@example.com', '6667778888', 'Staff', 40000.00),
(5, 'Alex Turner', 'alex@example.com', '2223334444', 'Staff', 40000.00);
select * from employee;

INSERT INTO Location VALUES 
(1, 'Warehouse A', '100 Warehouse Ave'),
(2, 'Warehouse B', '200 Storage St'),
(3, 'Warehouse C', '300 Distribution Blvd'),
(4, 'Main Office', '400 Corporate Ave'),
(5, 'Local Store', '500 Retail St');
select * from location;

INSERT INTO Payment VALUES 
(1, 1, 3, 15.00, '2023-01-20'),
(2, 2, 1, 10.00, '2023-01-18'),
(3, 3, 4, 20.00, '2023-01-25'),
(4, 4, 2, 25.00, '2023-02-01'),
(5, 5, 5, 30.00, '2023-02-10');
select * from payment;

/*1*/
SELECT * FROM UserTable;

/*2*/
SELECT * FROM Courier WHERE courierid = 1;

/*3*/
select * from courier;

/*4*/
SELECT *
FROM Courier
WHERE CourierID = 5;

/*5*/
SELECT *
FROM Courier
WHERE Status = 'delivered';

/*6*/
SELECT *
FROM Courier
WHERE Status = 'undelivered';

/*7*/
SELECT *
FROM Courier
WHERE DeliveryDate = CURDATE();

/*8*/
SELECT *
FROM Courier
WHERE Status = 'Pending';

/*9*/
SELECT CourierID, COUNT(*) AS TotalPackages
FROM Courier
GROUP BY CourierID;

/*10*/
SELECT CourierID, AVG(DATEDIFF(DeliveryDate, CURDATE())) AS AvgDeliveryTime
FROM Courier
WHERE DeliveryDate IS NOT NULL
GROUP BY CourierID;

/*11*/
SELECT *
FROM Courier
WHERE Weight BETWEEN 2.0 AND 5.0;

/*12*/
SELECT *
FROM Employee
WHERE Name LIKE '%John%';

/*13*/
SELECT c.*
FROM Courier c
INNER JOIN Payment p ON c.CourierID = p.CourierID
WHERE p.Amount > 50.00;

/*task 3*/
/*14*/
SELECT e.EmployeeID, e.Name, 
    (SELECT COUNT(*) FROM Courier WHERE courierID = e.EmployeeID) AS TotalCouriersHandled
FROM Employee e;

/*15*/
SELECT l.LocationID, l.LocationName, SUM(p.Amount) AS TotalRevenue
FROM Location l
LEFT JOIN Payment p ON l.LocationID = p.LocationID
GROUP BY l.LocationID, l.LocationName;

/*16*/
SELECT l.LocationID, l.LocationName, COUNT(c.CourierID) AS TotalCouriersDelivered
FROM Location l
LEFT JOIN Courier c ON l.LocationID = c.LocationID
GROUP BY l.LocationID, l.LocationName;

/*17*/
SELECT CourierID, AVG(DATEDIFF(DeliveryDate, OrderDate)) AS AvgDeliveryTime
FROM Courier
WHERE DeliveryDate IS NOT NULL
GROUP BY CourierID
ORDER BY AvgDeliveryTime DESC
LIMIT 1;

/*18*/
SELECT l.LocationID, l.LocationName, SUM(p.Amount) AS TotalPayments
FROM Location l
LEFT JOIN Payment p ON l.LocationID = p.LocationID
GROUP BY l.LocationID, l.LocationName
HAVING COALESCE(SUM(p.Amount), 0) < 1000;

/*19*/
SELECT LocationID, SUM(Amount) AS TotalPayments
FROM Payment
GROUP BY LocationID;

/*20*/
SELECT c.*
FROM Courier c
INNER JOIN Payment p ON c.CourierID = p.CourierID
WHERE p.LocationID = 4
GROUP BY c.CourierID
HAVING SUM(p.Amount) > 1000

/*21*/
SELECT l.LocationID, l.LocationName, SUM(p.Amount) AS TotalAmountReceived
FROM Payment p
INNER JOIN Location l ON p.LocationID = l.LocationID
WHERE p.PaymentDate < '2023-02-10'
GROUP BY l.LocationID, l.LocationName
HAVING SUM(p.Amount) > 1000;

/*22*/
SELECT l.LocationID, l.LocationName, SUM(p.Amount) AS TotalAmountReceived
FROM Payment p
INNER JOIN Location l ON p.LocationID = l.LocationID
WHERE p.PaymentDate < '2023-02-10'
GROUP BY l.LocationID, l.LocationName
HAVING SUM(p.Amount) > 5000;

/*task-4*/
/*23*/
SELECT p.PaymentID, p.CourierID, p.Amount, p.PaymentDate, c.SenderName, c.ReceiverName, c.TrackingNumber
FROM Payment p
INNER JOIN Courier c ON p.CourierID = c.CourierID;

/*24*/
SELECT p.PaymentID, p.LocationID, p.Amount, p.PaymentDate, l.LocationName, l.Address
FROM Payment p
INNER JOIN Location l ON p.LocationID = l.LocationID;

/*25*/
SELECT p.PaymentID, p.CourierID, p.Amount AS PaymentAmount, p.PaymentDate,
       c.SenderName, c.ReceiverName, c.TrackingNumber,
       l.LocationID, l.LocationName, l.Address
FROM Payment p
INNER JOIN Courier c ON p.CourierID = c.CourierID
INNER JOIN Location l ON p.LocationID = l.LocationID;

/*26*/
SELECT p.PaymentID, p.CourierID, p.Amount, p.PaymentDate, c.SenderName, c.ReceiverName, c.TrackingNumber
FROM Payment p
INNER JOIN Courier c ON p.CourierID = c.CourierID;

/*27*/
SELECT c.CourierID, c.SenderName, c.ReceiverName, c.TrackingNumber, SUM(p.Amount) AS TotalPaymentsReceived
FROM Courier c
LEFT JOIN Payment p ON c.CourierID = p.CourierID
GROUP BY c.CourierID, c.SenderName, c.ReceiverName, c.TrackingNumber;

/*28*/
SELECT * FROM Payment
WHERE PaymentDate = '2023-02-10';

/*29*/
SELECT p.PaymentID, p.Amount, p.PaymentDate, c.SenderName, c.ReceiverName, c.TrackingNumber
FROM Payment p
INNER JOIN Courier c ON p.CourierID = c.CourierID;

/*30*/
SELECT p.PaymentID, p.Amount, p.PaymentDate, l.LocationName, l.Address
FROM Payment p
INNER JOIN Location l ON p.LocationID = l.LocationID;

/*31*/
SELECT c.CourierID, c.SenderName, c.ReceiverName, SUM(p.Amount) AS TotalPayments
FROM Courier c
LEFT JOIN Payment p ON c.CourierID = p.CourierID
GROUP BY c.CourierID, c.SenderName, c.ReceiverName;

/*32*/
SELECT *
FROM Payment
WHERE PaymentDate BETWEEN '2023-02-5' AND '2023-02-10';

/*33*/
SELECT *
FROM Usertable u
LEFT JOIN Courier c ON u.userid = c.CourierID
UNION
SELECT *
FROM Usertable u
RIGHT JOIN Courier c ON u.userid = c.CourierID
WHERE u.userid IS NULL;

/*34*/
SELECT *
FROM Courier c
LEFT JOIN CourierServices cs ON c.ServiceID = cs.ServiceID
UNION
SELECT *
FROM Courier c
RIGHT JOIN CourierServices cs ON c.ServiceID = cs.ServiceID
WHERE c.ServiceID IS NULL; /* not connected*/

/*35*/
SELECT * FROM Employee e LEFT JOIN Payment p ON e.EmployeeID = p.EmployeeID
UNION SELECT * FROM Employee e RIGHT JOIN Payment p ON e.EmployeeID = p.EmployeeID
WHERE e.EmployeeID IS NULL;/*not connected*/

/*36*/
SELECT * FROM Usertable CROSS JOIN CourierServices;

/*37*/
SELECT *
FROM Employee
CROSS JOIN Location;

/*38*/
SELECT CourierID, SenderName, SenderAddress, SenderAddress
FROM Courier;

/*39*/
SELECT CourierID, ReceiverName, ReceiverAddress, Receiveraddress
FROM Courier;

/*40*/
SELECT c.CourierID, cs.ServiceName, cs.Cost
FROM Courier c
LEFT JOIN CourierServices cs ON c.ServiceID = cs.ServiceID;

/*41*/
SELECT e.EmployeeID, e.Name AS EmployeeName, COUNT(c.CourierID) AS NumberOfCouriers
FROM Employee e
LEFT JOIN Courier c ON e.EmployeeID = c.EmployeeID
GROUP BY e.EmployeeID, e.Name;

/*42*/
SELECT l.LocationID, l.LocationName, SUM(p.Amount) AS TotalPaymentAmount
FROM Location l
LEFT JOIN Payment p ON l.LocationID = p.LocationID
GROUP BY l.LocationID, l.LocationName
ORDER BY l.LocationID;

/*43*/
SELECT * FROM Courier
WHERE SenderName = (
    SELECT SenderName
    FROM Courier
    WHERE CourierID = 4);
    
/*44*/
SELECT * FROM Employee
WHERE Role = (SELECT Role FROM Employee WHERE EmployeeID = 5);
    
/*45*/
SELECT *
FROM Payment
WHERE CourierID IN (
    SELECT CourierID
    FROM Courier
    WHERE SenderAddress = (
        SELECT SenderAddress
        FROM Courier
        WHERE CourierID = 3));

/*46*/
SELECT *
FROM Courier
WHERE SenderAddress = (
    SELECT SenderAddress
    FROM Courier
    WHERE CourierID = 2);
    
/*47*/
SELECT e.EmployeeID, e.Name AS EmployeeName, COUNT(c.CourierID) AS NumberOfCouriersDelivered
FROM Employee e
LEFT JOIN Courier c ON e.EmployeeID = c.EmployeeID
GROUP BY e.EmployeeID, e.Name
ORDER BY e.EmployeeID;

/*48*/
SELECT *
FROM Courier c
INNER JOIN CourierServices cs ON c.ServiceID = cs.ServiceID
INNER JOIN Payment p ON c.CourierID = p.CourierID
WHERE p.Amount > cs.Cost;

/*49*/
SELECT *
FROM Courier
WHERE Weight > (
    SELECT AVG(Weight)
    FROM Courier);

/*50*/
SELECT Name
FROM Employee
WHERE Salary > (
    SELECT AVG(Salary)
    FROM Employee);
    
/*51*/
SELECT SUM(Cost) AS TotalCost
FROM CourierServices
WHERE Cost < (
    SELECT MAX(Cost)
    FROM CourierServices);
    
/*52*/
SELECT DISTINCT c.*
FROM Courier c
INNER JOIN Payment p ON c.CourierID = p.CourierID;

/*53*/
SELECT l.LocationName
FROM Location l
INNER JOIN Payment p ON l.LocationID = p.LocationID
WHERE p.Amount = (
    SELECT MAX(Amount)
    FROM Payment);
    
/*54*/
SELECT *
FROM Courier
WHERE Weight > (
    SELECT MAX(Weight)
    FROM Courier
    WHERE SenderName = '2');









































































