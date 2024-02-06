import mysql.connector as con
m1=con.connect(host="localhost",user="root",password="Root",port="3306")
cur=m1.cursor()
cur.execute("create database loan_management_system")