import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root" , passwd = "Paliwal@286")
print(mydb)

cursor = mydb.cursor()
cursor.execute("insert into sudhanshu.ineuron values(101, 'deepak', 'deepak@gmail.com', 100, 30)")
mydb.commit()
cursor.execute("select * from sudhanshu.ineuron")
for i in cursor.fetchall():
    print(i)