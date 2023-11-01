import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="Vinay12+"
)

print(mydb.is_connected())

cur = mydb.cursor()
# cur.execute("select brand_name, count(*) as 'total_phn', avg(price) as 'avg_price' ,max(rating) as 'max_rating',round(avg(screen_size),2) as 'avg_srn_size' from dml.mobile_phones group by brand_name order by total_phn desc limit 5")
# cur.execute("""select has_nfc,avg(price) as 'avg price' ,avg(rating) as 'avg rating' 
#                 from dml.mobile_phones
#                 group by has_nfc    
#         """)
# cur.execute("""select extended_memory_available,
#             avg(price) as 'avg price',
#             avg(rating) as 'rating'
#             from dml.mobile_phones
#             group by extended_memory_available
#         """)
# cur.execute("""select brand_name,processor_brand,
#             count(*) as 'num phones' ,avg(primary_camera_rear) as 'avg camera'
#             from dml.mobile_phones
#             group by brand_name,processor_brand

# """)
# cur.execute("""select brand_name,round(avg(price)) as 'avg_price' 
#             from dml.mobile_phones
#             group by brand_name
#             order by avg_price desc limit 5 """)
# cur.execute(""" select brand_name,round(avg(screen_size)) as 'avg_srn_sz'
#                 from dml.mobile_phones
#                 group by brand_name
#                 order by avg_srn_sz asc limit 5
#             """)
# cur.execute("""select brand_name,count(*) as count_
#             from dml.mobile_phones
#             where has_ir_blaster='True' and has_nfc='True'
#             group by brand_name
#             order by count_ desc limit 10
#                         """)
# cur.execute("""select brand_name,count(*) as 'count_',
#             round(avg(price )) as 'price_'
#             from dml.mobile_phones
#             group by brand_name 
#             having count_>20
#             order by price_ desc limit 10
            
#             """)
# cur.execute("""select brand_name, round(avg(rating)) as 'avg_rating',
#             count(*) as 'count_'
#             from dml.mobile_phones
#             group by brand_name
#             having count_>20
#             order by avg_rating desc limit 10

#             """)
# cur.execute("""select brand_name,avg(ram_capacity) as 'avg_ram'
#             from dml.mobile_phones
#             where refresh_rate>90 and fast_charging_available=1
#             group by brand_name
#             having count(*)>10 
#             order by 'avg_ram' desc limit 3

            


# """)
cur.execute("""select brand_name,avg(price) as 'avg_price' 
            from dml.mobile_phones
            where has_5g='True'
            group by brand_name
            having avg(rating)>70 and count(*)>10



""")



for i in cur:
    print(i)