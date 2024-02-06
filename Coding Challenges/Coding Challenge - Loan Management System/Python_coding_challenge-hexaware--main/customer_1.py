import mysql.connector as con
m1=con.connect(host="localhost",user="root",password="Root",database="loan_management_system",port="3306")
cur=m1.cursor()
q1="""
    CREATE TABLE Customer (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    email_address VARCHAR(60),
    phone_number VARCHAR(15),
    address VARCHAR(150),
    credit_score INT
);
"""

q2="""
ALTER TABLE Customer AUTO_INCREMENT=1;
"""

cur.execute(q1)
cur.execute(q2)
cur.close()