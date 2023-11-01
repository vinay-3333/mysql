import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vinay12+"
)

print(mydb.is_connected())
cur =mydb.cursor()
# cur.execute("CREATE DATABASE hello")

# cur.execute("""CREATE TABLE hello.user(
#             user_id integer primary key,
#             name varchar(255) not null,
#             age integer not null,
#             emergency_contact integer not null,
          
#             CONSTRAINT userid_name unique(name)
# ) """)

# cur.execute("""CREATE TABLE hello.group_(
#             group_id integer primary key,
#             group_name varchar(255) 
# )

# """)
# cur.execute("""insert into hello.user values(1,'nitish',34,11),
#             (2,'ankit',32,1),(3,'neha',23,1),(4,'rekha',34,3),
#             (5,'vinay',31,11)
# """)
# cur.execute("""insert into hello.group_ values(1,'group1'),
#             (2,'group2'),(3,"group3"),
#             (7,"group7")
#             """)     
# mydb.commit()

# cur.execute("select * from hello.user t1 cross join hello.group_ t2")

# cur.execute("""create table hello.membership(
#             member_id integer primary key ,
#             group_id integer,
#             user_id integer
# )""")
# cur.execute("""insert into hello.membership values(9,4,1),(2,1,2),
#              (3,1,3),(8,3,3),(4,1,4),(6,2,4),(10,2,4)""")
# mydb.commit()


# cur.execute("""select * from hello.membership t1 
#             inner join hello.user t2 on t1.user_id = t2.user_id""")
# cur.execute("""select * from hello.membership t1
#             left join hello.user t2 
#             on t1.user_id = t2.user""")
# cur.execute("""select * from hello.membership t1 
#             right join hello.user t2
#             on t1.user_id = t2.user_id""")

# cur.execute("""select * from hello.membership t1 
#             full outer join hello.user t2
#             on t1.user_id = t2.user_id""")


# cur.execute("""select * from hello.user t1
#             left join hello.membership t2 
#             on t1.user_id = t2.user
#             union
#             select * from hello.membership t1 
#             right join hello.user t2
#             on t1.user_id = t2.user_id""")

# cur.execute("create database flipkart")

# cur.execute("""create table flipkart.users(
#             user_id integer ,
#             name varchar(255),
#             age integer,
#             contact integer,
#         group_id integer,
#             group_name varchar(255)
# )""")

# cur.execute("""insert into flipkart.users values
#             (4,'radhika',34,3,7,'group_7'),
#             (8,'abhinav',31,11,1,'group_1'),
#             (8,'abhinav',31,11,2,'group_2'),
#             (8,'abhinav',31,11,3,'group_3'),
#             (8,'abhinav',31,11,7,'group_7'),
#             (11,'rahul',29,8,1,'group_1'),
#             (11,'rahul',29,8,2,'group_2'),
#             (11,'rahul',29,8,3,'group_3'),
#             (11,'rahul',29,8,7,'group_7')
# """)



# marge more then 1 table
# cur.execute("""select t1.order_id,t1.amount,t1.profit,t3.name 
#             from flipkar.order t1
#             join flipkart.orders t2
#             on t1.order_id = t2.order_id
#             join flipkart.user t3
#             on t2.user_id =t3.user_id


# """)


# cur.execute("""select * from flipkart.orders t1
#             join flipkart.users t2
#             on t1.user_id = t2.user_id
#             where t2.city ='Pune'

# """)


# find all profitable orders
# cur.execute("""select t1.order_id,sum(t2.profit)
#             from flipkart.order t1
#             join flipkart.order_details t2
#             on t1.order_id = t2.order_id
#             group by t1.order_id
#             having sum(t2.profit)>0

# """)


# find max number of order from user
# cur.execute("""select name,count(*) from flipkart.orders t1
#             join flipkart.users t2 
#             on t1.user_id = t2.user_id
#             group by t2.name
#             order by count(*) desc limit 1

# """)


# which most profitable categoriy
# cur.execute("""select t2.vartical,sum(profit) from flipkart.order_details t1
#             join flipkart.category t2
#             on t1.category_id = t2.category_id
#             group by t2.vertical
#             order by sum(profit ) desc limit 1

# """)