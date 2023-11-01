import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="Vinay12+"
)

print(mydb.is_connected())

cur = mydb.cursor()
# cur.execute("select DISTINCT(brand_name) dml.mobile_phones where price > 50000")
# cur.execute("SELECT * FROM dml.mobile_phones WHERE processor_brand IN ('snapdragon','exynos')")
# cur.execute("SELECT * FROM dml.mobile_phones WHERE processor_brand NOT IN ('snapdragon','exynos')")
# cur.execute("Update dml.mobile_phones SET processor_brand ='dimensity' WHERE processor_brand='mediatek' ")
# cur.execute("DELETE from dml.mobile_phones where price >200000")
# cur.execute("select * from dml.mobile_phones where primary_camera_rear>150  and brand_name='samsung' ")
# cur.execute("select max(price) from dml.mobile_phones")
# cur.execute("select max(ram_capacity) from dml.mobile_phones")
# cur.execute("select min(ram_capacity) from dml.mobile_phones")
# cur.execute("select max(price) from dml.mobile_phones where brand_name='samsung' ")
# for i in cur:
#     print(i)
# cur.execute("select avg(rating) from dml.mobile_phones where brand_name ='apple' ")
# cur.execute("select avg(price) from dml.mobile_phones where brand_name='apple' ")
# cur.execute("select sum(price) from dml.mobile_phones where brand_name='apple' ")
# for i in cur:
#     print(i)
# cur.execute("select count(*) from dml.mobile_phones where brand_name='oneplus' ")
# cur.execute("select count(DISTINCT(brand_name)) from dml.mobile_phones")
# for i in cur:
#     print(i)

# cur.execute("select model, screen_size from dml.mobile_phones where brand_name='samsung' order by screen_size DESC Limit 10 ")
# cur.execute("""select model,num_rear_cameras+num_front_cameras AS 'total_cmra' 
#             from dml.mobile_phones order by total_cmra desc """)
# cur.execute("select model,battery_capacity from dml.mobile_phones order by battery_capacity desc limit 1,1")
# cur.execute("select model,rating from dml.mobile_phones where brand_name ='apple'  order by rating asc limit 5 ")
cur.execute("select model,rating from dml.mobile_phones order by brand_name asc ,rating desc ")


for i in cur:
    print(i)