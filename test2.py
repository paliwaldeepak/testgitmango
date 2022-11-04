import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root" , passwd = "Paliwal@286")
print(mydb)

cursor = mydb.cursor()
#cursor.execute("create database sudhanshu")
#cursor.execute("create table sudhanshu.ineuron(employee_id int(10), employee_name varchar(80), emp_mailid varchar(20), emp_salary int(6) , emp_attendence int(3))")
#cursor.execute("show databases")

q1 = cursor.execute("select * from sudhanshu.ineuron")
print(q1)