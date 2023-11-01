import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="Vinay12+"
)

print(mydb.is_connected())

cur = mydb.cursor()
#cur.execute("CREATE DATABASE DML")
#cur.execute("""CREATE TABLE DML.user(
            #user_id INTEGER PRIMARY KEY AUTO_INCREMENT,
           # name VARCHAR(255) NOT NULL, 
           # email VARCHAR(255) NOT NULL,     
          #  password VARCHAR(255) NOT NULL,
         #   CONSTRAINT unique_email UNIQUE(email)   
#)""")

#cur.execute("""INSERT INTO campusx.user(user_id,name,email,password)
 #            VALUES(NULL,"vinay","vagrawal@gmail.com","sfsfsfs")""")
#cur.execute("CREATE TABLE campusx.smartphone(df.head(1))")

'''create_table_sql = """
CREATE TABLE dml.mobile_phones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand_name VARCHAR(255),
    model VARCHAR(255),
    price DECIMAL(10, 2),
    rating DECIMAL(3, 1),
    has_5g BOOLEAN,
    has_nfc BOOLEAN,
    has_ir_blaster BOOLEAN,
    processor_brand VARCHAR(255),
    num_cores DECIMAL(3, 1),
    processor_speed DECIMAL(5, 2),
    battery_capacity DECIMAL(6, 1),
    fast_charging_available BOOLEAN,
    fast_charging DECIMAL(5, 2),
    ram_capacity DECIMAL(6, 1),
    internal_memory DECIMAL(6, 1),
    screen_size DECIMAL(4, 2),
    refresh_rate INT,
    num_rear_cameras INT,
    num_front_cameras DECIMAL(3, 1),
    os VARCHAR(255),
    primary_camera_rear DECIMAL(5, 2),
    primary_camera_front DECIMAL(5, 2),
    extended_memory_available BOOLEAN,
    extended_upto DECIMAL(6, 1),
    resolution_width INT,
    resolution_height INT
);
"""
df = pd.read_csv("smartphones_cleaned_v6.csv")
cur.execute(create_table_sql)
# Execute the table creation SQL statement
#cursor.execute(create_table_sql)

# Commit the changes to the database
#connection.commit()

# Read the data from the CSV file using Pandas
csv_file_path = "C:\data science\database python\smartphones_cleaned_v6.csv"  # Replace with the actual file path
df = pd.read_csv(csv_file_path)

# Define the data insertion SQL statement (same as before)
insert_data_sql = """
INSERT INTO dml.mobile_phones (
    brand_name, model, price, rating, has_5g, has_nfc, has_ir_blaster,
    processor_brand, num_cores, processor_speed, battery_capacity,
    fast_charging_available, fast_charging, ram_capacity, internal_memory,
    screen_size, refresh_rate, num_rear_cameras, num_front_cameras, os,
    primary_camera_rear, primary_camera_front, extended_memory_available,
    extended_upto, resolution_width, resolution_height
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

# Convert the Pandas DataFrame to a list of tuples for insertion
data = [tuple(row) for row in df.values]

# Insert data into the table
cur.executemany(insert_data_sql, data)
mydb.commit()'''
# cur.execute('SELECT * FROM dml.mobile_phones ')
# for i in cur:
#     print(i)
# cur.execute("SELECT os AS 'operatingsystem',model,battery_capacity AS 'MaH' FROM dml.mobile_phones")
# for i in cur:
#     print(i)
# cur.execute("""SELECT model,
#             SQRT(resolution_width*resolution_width+resolution_height*resolution_height)/screen_size AS 'PPI'
#             FROM dml.mobile_phones
# """)
# for i in cur:
#     print(i)

# # for create new col and put value command
# # cur.execute("SELECT model ,'samartphone' AS 'type' FROM dml.mobile_phones")
# cur.execute("SELECT DISTINCT(processor_brand) AS 'all processor' FROM dml.mobile_phones")
# cur.execute("SELECT DISTINCT brand_name,processor_brand FROM dml.mobile_phones")
# mydb.commit()
# for i in cur:
#     print(i)


# cur.execute("SELECT * FROM dml.mobile_phones where brand_name ='samsung'")
# cur.execute("SELECT * FROM dml.mobile_phones where price>50000")
# for i in cur:
#     print(i)
# cur.execute("SELECT * FROM dml.mobile_phones where price BETWEEN 10000 AND 20000")
# cur.execute("SELECT * FROM dml.mobile_phones where price <25000 AND rating>80")
cur.execute("select DISTINCT(brand_name) dml.mobile_phones where price > 50000")