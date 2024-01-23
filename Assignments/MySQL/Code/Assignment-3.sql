show databases;
create database bankingsystem;
show databases;
use bankingsystem;

create table Customers(customer_id int,first_name text,last_name text,DOB date,email text,phone_number int,address text, primary key(customer_id));
desc customers;

create table Accounts(account_id int,customer_id int,account_type text,balance bigint,
primary key(account_id),foreign key(customer_id) references customers(customer_id));
desc accounts;

create table transactions(transaction_id int,account_id int,transaction_type text,amount bigint,
transaction_date date, primary key(transaction_id),foreign key(account_id) references accounts(account_id)); 
desc transactions;

insert into customers values(1,"Alex","Johnson","1968-11-15","alex.carter@email.com", 1234567890,"Rivertown");
insert into customers values(2, "Jordan", "Davis","1972-12-3","jordan.anderson@email.com", 1234568790, "Summitville"),
(3, "Morgan", "Turner","1985-3-12","morgan.r@email.com", 1234567890, "Lakeside"),
(4, "Casey", "Hayes","1965-3-23","casey.t@email.com", 1234567890, "Pineville"),
(5, "Riley", "Martin","1995-10-5","riley.p@email.com", 1234567890, "Crestwood"),
(6, "Avery", "Reed","1983-9-15","avery.s@email.com", 1234567890, "Brookside"),
(7, "Quinn", "Jackson","1973-4-19","quinn.c@email.com", 1234567890, "Ridgefield"),
(8, "Cameron", "Fisher","1999-3-8","cameron.w@email.com", 1234567890, "Greenfield"),
(9, "Morgan", "Robinson","1987-4-7","morgan.b@email.com",1234567890, "Fairfield"),
(10, "Taylor", "Walker","1993-6-12","taylor.m@email.com", 1234567890, "Harbor City");
select * from customers;

insert into accounts values(1,10,"current",1025452),(2,9,"savings",13544),(3,8,"zero-balance",10254),
(4,7,"current",64364),(5,6,"current",10252),(6,5,"savings",25452),(7,4,"zero-balance",3452),
(8,3,"current",15452),(9,2,"zer-balance",25452),(10,1,"savings",543324);
select * from accounts;

insert into transactions values(1,10,"deposit",12343,"2023-12-4"),(2,9,"withdrawal",13343,"2023-12-1"),
(3,8,"transfer",2345,"2023-12-2"),(4,7,"deposit",34522,"2023-5-21"),(5,6,"transfer",8976,"2023-5-4"),
(6,5,"deposit",4532,"2023-6-3"),(7,4,"withdrawal",2356,"2023-1-4"),(8,3,"withdrawal",1234,"2023-12-4"),
(9,2,"deposit",1234,"2023-2-4"),(10,1,"transfer",1200,"2022-12-4");
select * from transactions;

/* 1 */
select concat(first_name," ",Last_name) as full_name, Email, account_type
from customers c, accounts a
where c.customer_id=a.customer_id;

/* 2 */
SELECT c.customer_id, c.first_name, c.last_name, t.transaction_id, t.transaction_type, t.amount, t.transaction_date
FROM customers c
JOIN accounts a ON c.customer_id = a.customer_id
JOIN transactions t ON a.account_id = t.account_id
ORDER BY c.customer_id, t.transaction_date;


/* 3*/
UPDATE Accounts
SET balance = balance + 500 
WHERE account_id = 1; 
select * from accounts;

/*4*/
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM Customers;
select * from customers;

/*5*/
DELETE FROM Accounts WHERE balance = 0 AND account_type = 'savings';
select * from accounts;

/*6*/
SELECT * FROM Customers WHERE address LIKE '123 pune';

/*7*/
SELECT balance FROM Accounts WHERE account_id = 1; 

/*8*/
SELECT * FROM Accounts WHERE account_type = 'current' AND balance > 1000;

/*9*/
SELECT * FROM Transactions WHERE account_id = 1;

/*10*/
SELECT account_id, balance * 0.05 AS interest_accured
FROM Accounts
WHERE account_type = 'savings';

/*11*/
SELECT *
FROM Accounts
WHERE balance < -1000;

/*12*/
SELECT *
FROM Customers
WHERE address NOT LIKE '123 pune'; 

/*task 3*/
/*1*/
SELECT AVG(balance) AS average_balance
FROM Accounts;

/*2*/
SELECT customer_id, account_id, balance
FROM Accounts
ORDER BY balance DESC
LIMIT 10;

/*3*/
SELECT SUM(amount) AS total_deposits
FROM Transactions
WHERE transaction_type = 'deposit' AND transaction_date = '2023-02-15';

/*4*/
SELECT MIN(DOB) AS oldest_customer, MAX(DOB) AS newest_customer
FROM Customers;

/*5*/
SELECT customer_id, COUNT(*) AS num_accounts
FROM Accounts
GROUP BY customer_id
HAVING COUNT(*) > 1;

/*6*/
SELECT transaction_type, SUM(CASE WHEN transaction_type = 'deposit' THEN amount ELSE -amount END) AS net_amount
FROM Transactions
GROUP BY transaction_type;

/*10*/
SELECT account_id, AVG(balance) AS average_daily_balance
FROM Accounts
GROUP BY account_id;

/*11*/
SELECT account_type, SUM(balance) AS total_balance
FROM Accounts
GROUP BY account_type;

/*12*/
SELECT account_id, COUNT(*) AS transaction_count
FROM transactions
GROUP BY account_id
ORDER BY COUNT(*) DESC;

/*13*/
SELECT c.customer_id, c.first_name, c.last_name, a.account_type, SUM(a.balance) AS total_balance
FROM customers c
JOIN accounts a ON c.customer_id = a.customer_id
GROUP BY c.customer_id, a.account_type
ORDER BY total_balance DESC;

/*14*/
SELECT t1.transaction_id, t1.account_id, t1.amount, t1.transaction_date
FROM transactions t1
JOIN transactions t2 ON t1.amount = t2.amount
AND t1.transaction_date = t2.transaction_date
AND t1.account_id = t2.account_id
WHERE t1.transaction_id <> t2.transaction_id
ORDER BY t1.amount, t1.transaction_date, t1.account_id;

/*task 4*/
/*1*/
SELECT c.customer_id, c.first_name, c.last_name, SUM(a.balance) AS total_balance
FROM customers c
JOIN accounts a ON c.customer_id = a.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_balance DESC
LIMIT 1;

/*2*/
SELECT AVG(sub.total_balance) AS average_balance
FROM (
    SELECT c.customer_id, SUM(a.balance) AS total_balance, COUNT(*) AS account_count
    FROM customers c
    JOIN accounts a ON c.customer_id = a.customer_id
    GROUP BY c.customer_id
    HAVING account_count > 1
) AS sub;

/*3*/
SELECT t.account_id, t.transaction_id, t.amount, AVG(t.amount) OVER () AS avg_transaction_amount
FROM transactions t
WHERE t.amount > (SELECT AVG(amount) FROM transactions);

/*4*/
SELECT c.customer_id, c.first_name, c.last_name
FROM customers c
LEFT JOIN transactions t ON c.customer_id = t.account_id
WHERE t.account_id IS NULL;

/*5*/
SELECT COALESCE(SUM(a.balance), 0) AS total_balance_no_transactions
FROM accounts a
LEFT JOIN transactions t ON a.account_id = t.account_id
WHERE t.account_id IS NULL;

/*6*/
SELECT *
FROM transactions
WHERE account_id IN (
    SELECT account_id
    FROM accounts
    WHERE balance = (
        SELECT MIN(balance)
        FROM accounts));
        
/*7*/
SELECT c.customer_id, c.first_name, c.last_name
FROM customers c
JOIN accounts a ON c.customer_id = a.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING COUNT(DISTINCT a.account_type) > 1;

/*8*/
SELECT account_type,
       COUNT(*) AS number_of_accounts,
       ROUND((COUNT(*) * 100.0) / (SELECT COUNT(*) FROM accounts), 2) AS percentage
FROM accounts
GROUP BY account_type;

/*9*/
SELECT t.transaction_id, t.account_id, t.transaction_type, t.amount, t.transaction_date
FROM transactions t
JOIN accounts a ON t.account_id = a.account_id
WHERE a.customer_id = 5;

/*10*/
SELECT account_type,
    (SELECT COALESCE(SUM(balance), 0) FROM accounts a WHERE a.account_type = accounts.account_type) AS total_balance
FROM accounts 
GROUP BY account_type;































