import mysql.connector as con
m1=con.connect(host="localhost",user="root",password="Root",database="loan_management_system",port="3306")
cur=m1.cursor()
q1="""
   CREATE TABLE Loan (
    loan_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id) on DELETE CASCADE,
    principal_amount Decimal(10, 2),
    interest_rate INT,
    loan_term INT,
    loan_type VARCHAR(20),
    loan_status VARCHAR(20)    
);
"""

q2="""
ALTER TABLE Loan AUTO_INCREMENT=101;
"""

cur.execute(q1)
cur.execute(q2)
cur.close()