import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="Vinay12+"
)

print(mydb.is_connected())

cur = mydb.cursor()
# cur.execute("create database std_info")
# cur.execute("create table std_info.std (id int , name varchar(50), phone int(50))")
cur.execute("insert into std_info.std values(123,'vinay',3456)")
mydb.commit()
cur.execute("select * from std_info.std")
for i in cur:
    print(i)