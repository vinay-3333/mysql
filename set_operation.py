import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vinay12+"
)

print(mydb.is_connected())
cur =mydb.cursor()


# cur.execute("drop database person2")
# cur.execute("drop database person1")
# cur.execute("create database person")
# cur.execute("create table person.person1(id integer ,name varchar(255))")
# cur.execute("create table person.person2(id integer ,name varchar(255))")
# cur.execute("insert into person.person1 values(1,'hemant'),(2,'niraj'),(3,'lalita')")
# cur.execute("insert into person.person1 values(3,'lalita'),(4,'dada'),(5,'rajemdra')")
# cur.execute("""select * from person.person1
#             union
#             select * from person.person2
#             """)
# cur.execute("""select * from person.person1
#             union all
#             select * from person.person2
#             """)

# cur.execute("""select * from person.person1
#             intersect
#             select * from person.person2
#             """)
# cur.execute("""select * from person.person1
#             except
#             select * from person.person2
#             """)