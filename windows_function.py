import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="Vinay12+"
)

print(mydb.is_connected())

cur = mydb.cursor()
# cur.execute("create database new_data")
# cur.execute("""CREATE TABLE new_data.marks (
#             student_id INTEGER PRIMARY KEY AUTO_INCREMENT,
#             name VARCHAR(255),
#             branch VARCHAR(255),
#             marks INTEGER
# )
# """)


# cur.execute("""INSERT INTO new_data.marks (name,branch,marks)VALUES 
# ('Nitish','EEE',82),
# ('Rishabh','EEE',91),
# ('Anukant','EEE',69),
# ('Rupesh','EEE',55),
# ('Shubham','CSE',78),
# ('Ved','CSE',43),
# ('Deepak','CSE',98),
# ('Arpan','CSE',95),
# ('Vinay','ECE',95),
# ('Ankit','ECE',88),
# ('Anand','ECE',81),
# ('Rohit','ECE',95),
# ('Prashant','MECH',75),
# ('Amit','MECH',69),
# ('Sunny','MECH',39),
# ('Gautam','MECH',51)
# """)
# mydb.commit()

# cur.execute("""select * ,avg(marks) over(partition by branch) from new_data.marks
# """)
# for i in cur:
#     print(i)


# cur.execute("""select * ,min(marks) over(partition by branch),
#             max(marks) over(partition by branch)
#             from new_data.marks
#             order by student_id  
# """)

# cur.execute("""select * from ( select *, avg(marks) over(partition by branch) as 'avg_bn'
#                 from new_data.marks )t1 
#                 where t1.marks > t1.avg_bn
              
# """)

# cur.execute("""select *,rand() over(partition by branch order by marks desc)
# #             from new_data.marks
# # """)


# cur.execute("""select *,rand() over(partition by branch order by marks desc)
#             dense_rank() over(partition by branch order by marks desc)
#             from new_data.marks
# """)

# cur.execute("""select *,
#             rank_number() over(partition by branch)
#             from new_data.marks""")


# cur.execute("""select *,
#             concat(branch,'-',rank_number() over(partition by branch))
#             from new_data.marks""")


# cur.execute("""select *  from (select monthname(data) as 'month',user_id,sum(amount) as 'total'
#             rank() over(partition by monthname(date) order by sum(amount) desc) as 'month_rank'
#             from order
#             group by monthname(data),user_id
#             order by month(date)) t
#             where t.month<3
#             order by month desc ,month_rank asc
# """) 



# cur.execute("""select *,
#             first_value(marks) over(order by marks desc)
#             from new_data.marks
# """)


# cur.execute("""select *,
#             last_value(marks) over(order by marks desc)
#             from new_data.marks
# """)


# cur.execute("""select *,
#             last_value(marks) over(partition by branch order by marks desc
#                                 rows between unbounded preceding and unbounded following)
#             from new_data.marks
# """)

cur.execute("""select *,
            nth_value(marks,2) over(partition by branch order by marks desc
                                rows between unbounded preceding and unbounded following)
            from new_data.marks
""")
for i in cur:
    print(i)

