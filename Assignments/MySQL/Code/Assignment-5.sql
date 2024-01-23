create database ticketbookingsystem;
use ticketbookingsystem;

create table venuetable(venue_id int primary key, venue_name varchar(200),address varchar(200));
desc venuetable;
show tables;

create table customertable(customer_id int primary key,customer_name varchar(200),email varchar(200),
phone_number varchar(20),booking_id int);
desc customertable;

create table eventtable(event_id int primary key, event_name varchar(200),event_date date,event_time time,
venue_id int,total_seats int,available_seats int, ticket_price decimal(8,2),event_type varchar(200),
booking_id int);
desc eventtable;

create table bookingtable(booking_id int primary key,customer_id int,event_id int,num_tickets int, totalcost decimal(8,2),
booking_date date);
desc bookingtable;

alter table eventtable
add foreign key(booking_id) references bookingtable(booking_id);
desc eventtable;

alter table customertable
add foreign key(booking_id) references bookingtable(booking_id);
desc customertable;

alter table bookingtable
add foreign key(customer_id) references customertable(customer_id),
add foreign key(event_id) references eventtable(event_id);
desc bookingtable;
/*task 2*/
/*1*/

INSERT INTO venuetable (venue_id, venue_name, address) VALUES
(1, 'Venue 1', 'Address 1'),
(2, 'Venue 2', 'Address 2'),
(3, 'Venue 3', 'Address 3'),
(4, 'Venue 4', 'Address 4'),
(5, 'Venue 5', 'Address 5'),
(6, 'Venue 6', 'Address 6'),
(7, 'Venue 7', 'Address 7'),
(8, 'Venue 8', 'Address 8'),
(9, 'Venue 9', 'Address 9'),
(10, 'Venue 10', 'Address 10');
select * from venuetable;

INSERT INTO customertable (customer_id, customer_name, email, phone_number, booking_id) VALUES
(1, 'John Doe', 'john@example.com', '1234567890', 101),
(2, 'Jane Smith', 'jane@example.com', '9876543210', 102),
(3, 'Alice Johnson', 'alice@example.com', '5555555555', 103),
(4, 'Bob Anderson', 'bob@example.com', '7777777777', 104),
(5, 'Ella Williams', 'ella@example.com', '3333333333', 105),
(6, 'Mike Brown', 'mike@example.com', '6666666666', 106),
(7, 'Sarah Wilson', 'sarah@example.com', '4444444444', 107),
(8, 'David Garcia', 'david@example.com', '2222222222', 108),
(9, 'Sophia Martinez', 'sophia@example.com', '8888888888', 109),
(10, 'William Lee', 'william@example.com', '9999999999', 110);
select * from customertable;

INSERT INTO eventtable (event_id, event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type, booking_id) VALUES
(1, 'Concert A', '2023-01-15', '18:00:00', 1, 1000, 500, 50.00, 'Music', 101),
(2, 'Conference X', '2023-02-20', '09:00:00', 2, 500, 250, 100.00, 'Business', 102),
(3, 'Play Y', '2023-03-10', '15:30:00', 3, 300, 150, 25.00, 'Theatre', 103),
(4, 'Festival Z', '2023-04-05', '12:00:00', 4, 800, 400, 75.00, 'Music', 104),
(5, 'Seminar B', '2023-05-18', '10:00:00', 5, 200, 100, 40.00, 'Education', 105),
(6, 'Comedy Show C', '2023-06-22', '20:00:00', 6, 400, 200, 30.00, 'Comedy', 106),
(7, 'Exhibition D', '2023-07-12', '11:00:00', 7, 600, 300, 20.00, 'Art', 107),
(8, 'Dance Event E', '2023-08-30', '19:30:00', 8, 700, 350, 60.00, 'Dance', 108),
(9, 'Tech Summit F', '2023-09-25', '09:30:00', 9, 400, 200, 85.00, 'Technology', 109),
(10, 'Magic Show G', '2023-10-14', '17:00:00', 10, 150, 75, 45.00, 'Entertainment', 110);
select * from eventtable;

INSERT INTO bookingtable (booking_id, customer_id, event_id, num_tickets, totalcost, booking_date) VALUES
(101, 1, 1, 2, 100.00, '2023-01-10'),
(102, 2, 3, 5, 125.00, '2023-02-18'),
(103, 3, 5, 3, 120.00, '2023-03-08'),
(104, 4, 7, 4, 80.00, '2023-04-01'),
(105, 5, 9, 1, 85.00, '2023-05-15'),
(106, 6, 2, 3, 300.00, '2023-06-20'),
(107, 7, 4, 2, 150.00, '2023-07-10'),
(108, 8, 6, 6, 180.00, '2023-08-25'),
(109, 9, 8, 5, 300.00, '2023-09-20'),
(110, 10, 10, 4, 180.00, '2023-10-10');
select * from bookingtable;

/*2*/
SELECT * FROM eventtable;

/*3*/
SELECT * 
FROM eventtable
WHERE available_seats > 0;

/*4*/
SELECT * 
FROM eventtable
WHERE event_name LIKE '%cup%';

/*5*/
SELECT * 
FROM eventtable
WHERE ticket_price BETWEEN 1000 AND 2500;

/*6*/
SELECT *
FROM eventtable
WHERE event_date BETWEEN '2023-01-01' AND '2023-12-31';

/*7*/
SELECT *
FROM eventtable
WHERE available_seats > 0
AND event_name LIKE '%Concert%';

/*8*/
SELECT * FROM customertable
ORDER BY customer_id
LIMIT 5 OFFSET 5;

/*9*/
SELECT *
FROM bookingtable AS b
JOIN eventtable AS e ON b.event_id = e.event_id
WHERE b.num_tickets > 4;

/*10*/
SELECT *
FROM customertable
WHERE phone_number LIKE '%000';

/*11*/
SELECT *
FROM eventtable
WHERE total_seats > 15000
ORDER BY total_seats DESC;

/*12*/
SELECT *
FROM eventtable
WHERE event_name NOT LIKE 'c%' 
AND event_name NOT LIKE 'a%'
AND event_name NOT LIKE 'z%';

/*task-3*/
/*1*/
SELECT e.event_id, e.event_name, AVG(b.ticket_price) AS average_ticket_price
FROM eventtable e
JOIN eventtable b ON e.event_id = b.event_id
GROUP BY e.event_id, e.event_name;

/*2*/
SELECT SUM(totalcost) AS total_revenue_generated
FROM bookingtable;

/*3*/
SELECT event_id, SUM(num_tickets) AS total_tickets_sold
FROM bookingtable
GROUP BY event_id
ORDER BY total_tickets_sold DESC
LIMIT 1;

/*4*/
SELECT event_id, SUM(num_tickets) AS total_tickets_sold
FROM bookingtable
GROUP BY event_id;

/*5*/
SELECT e.event_id, e.event_name
FROM eventtable e
LEFT JOIN bookingtable b ON e.event_id = b.event_id
WHERE b.event_id IS NULL;

/*6*/
SELECT customer_id, COUNT(*) AS total_tickets_booked
FROM bookingtable
GROUP BY customer_id
ORDER BY total_tickets_booked DESC
LIMIT 1;

/*7*/
SELECT 
    e.event_id,
    e.event_name,
    MONTH(b.booking_date) AS month_number,
    YEAR(b.booking_date) AS year_number,
    SUM(b.num_tickets) AS total_tickets_sold
FROM eventtable e
LEFT JOIN bookingtable b ON e.event_id = b.event_id
GROUP BY e.event_id, month_number, year_number
ORDER BY year_number, month_number;

/*8*/
SELECT v.venue_id, v.venue_name, AVG(e.ticket_price) AS average_ticket_price
FROM venuetable v
JOIN eventtable e ON v.venue_id = e.venue_id
GROUP BY v.venue_id, v.venue_name;

/*9*/
SELECT e.event_type, SUM(b.num_tickets) AS total_tickets_sold
FROM eventtable e
JOIN bookingtable b ON e.event_id = b.event_id
GROUP BY e.event_type;

/*10*/
SELECT YEAR(b.booking_date) AS event_year, SUM(b.totalcost) AS total_revenue
FROM bookingtable b
GROUP BY event_year;

/*11*/
SELECT customer_id, COUNT(DISTINCT event_id) AS num_events_booked
FROM bookingtable
GROUP BY customer_id
HAVING COUNT(DISTINCT event_id) > 1;

/*12*/
SELECT customer_id, SUM(totalcost) AS total_revenue_generated
FROM bookingtable
GROUP BY customer_id;

/*13*/
SELECT v.venue_id, v.venue_name, e.event_type, AVG(e.ticket_price) AS average_ticket_price
FROM venuetable v
JOIN eventtable e ON v.venue_id = e.venue_id
GROUP BY v.venue_id, v.venue_name, e.event_type;

/*14*/
SELECT customer_id, COUNT(*) AS total_tickets_purchased
FROM bookingtable
WHERE booking_date >= DATE_SUB(NOW(), INTERVAL 30 DAY)
GROUP BY customer_id;

/*task-4*/
/*1*/
SELECT v.venue_id, v.venue_name, AVGPrice.avg_ticket_price AS average_ticket_price
FROM venuetable v
JOIN (
    SELECT venue_id, AVG(ticket_price) AS avg_ticket_price
    FROM eventtable
    GROUP BY venue_id
) AS AVGPrice ON v.venue_id = AVGPrice.venue_id;

/*2*/
SELECT event_id, event_name
FROM eventtable
WHERE (
    SELECT SUM(num_tickets)
    FROM bookingtable
    WHERE bookingtable.event_id = eventtable.event_id) > 0.5 * total_seats;

/*3*/
SELECT e.event_id, e.event_name, SUM(b.num_tickets) AS total_tickets_sold
FROM eventtable e
LEFT JOIN bookingtable b ON e.event_id = b.event_id
GROUP BY e.event_id, e.event_name;

/*4*/
SELECT customer_id, customer_name
FROM customertable c
WHERE NOT EXISTS (
    SELECT 1
    FROM bookingtable b
    WHERE b.customer_id = c.customer_id);
    
/*5*/
SELECT event_id, event_name
FROM eventtable
WHERE event_id NOT IN (
    SELECT DISTINCT event_id
    FROM bookingtable);
    
/*6*/
SELECT e.event_type, COALESCE(bt.total_tickets_sold, 0) AS total_tickets_sold
FROM eventtable e
LEFT JOIN (
    SELECT event_id, SUM(num_tickets) AS total_tickets_sold
    FROM bookingtable
    GROUP BY event_id
) AS bt ON e.event_id = bt.event_id;

/*7*/
SELECT event_id, event_name, ticket_price
FROM eventtable
WHERE ticket_price > (
    SELECT AVG(ticket_price)
    FROM eventtable);
    
/*8*/
SELECT c.customer_id, c.customer_name,
(SELECT COALESCE(SUM(b.totalcost), 0)
FROM bookingtable b
WHERE b.customer_id = c.customer_id) AS total_revenue_generated
FROM customertable c;

/*9*/
SELECT DISTINCT c.customer_id, c.customer_name
FROM customertable c
WHERE c.customer_id IN (
    SELECT DISTINCT b.customer_id
    FROM bookingtable b
    JOIN eventtable e ON b.event_id = e.event_id
    WHERE e.venue_id = 5);
    
/*10*/
SELECT e.event_type, COALESCE(SUM(bt.total_tickets_sold), 0) AS total_tickets_sold
FROM eventtable e
LEFT JOIN (
    SELECT event_id, SUM(num_tickets) AS total_tickets_sold
    FROM bookingtable
    GROUP BY event_id
) AS bt ON e.event_id = bt.event_id
GROUP BY e.event_type;

/*11*/
SELECT DISTINCT c.customer_id, c.customer_name, MONTH(b.booking_date) AS booking_month
FROM customertable c
JOIN bookingtable b ON c.customer_id = b.customer_id
GROUP BY c.customer_id, booking_month;

/*12*/
SELECT v.venue_id, v.venue_name, COALESCE(avg_price.avg_ticket_price, 0) AS average_ticket_price
FROM venuetable v
LEFT JOIN (
    SELECT venue_id, AVG(ticket_price) AS avg_ticket_price
    FROM eventtable
    GROUP BY venue_id
) AS avg_price ON v.venue_id = avg_price.venue_id;














































