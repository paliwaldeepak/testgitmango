import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root" , passwd = "Paliwal@286")
print(mydb)

cursor = mydb.cursor()
cursor.execute("show databases")
print(cursor.fetchall())
