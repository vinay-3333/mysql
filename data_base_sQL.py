import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="Vinay12+"
)

print(mydb.is_connected())

cur = mydb.cursor()
cur.execute("show databases")
for i in cur:    
    print(i)