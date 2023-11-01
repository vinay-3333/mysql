import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="Vinay12+"
)

print(mydb.is_connected())

cur = mydb.cursor()
# cur.execute("CREATE DATABASE IF NOT EXISTS campusx")
# cur.execute("DROP DATABASE IF EXISTS campusx")
# cur.execute("""CREATE TABLE IF NOT EXISTS campusx.user(
        #   user_id INTEGER,
        #   name VARCHAR(255),
        #   email VARCHAR(255),
        #   password VARCHAR(255))""")
# cur.execute("DROP TABLE campusx.user")

# cur.execute("INSERT INTO campusx.user values(1,'vinay','vagrawal','fsddkfs'),(2,'hemant','hemant032','dfsf'),(3,'niraj','nirajsfks','dfsfs')")
# cur.execute("TRUNCATE TABLE campusx.user")
# cur.execute("""CREATE TABLE IF NOT EXISTS campusx.std(
            # user_id INTEGER NOT NULL,
            # name VARCHAR(255) NOT NULL,
            # email VARCHAR(255),
            # password VARCHAR(255)
# )""")

# cur.execute('INSERT INTO campusx.std values(1,"vinay","sfs@fsd","sfsfs")')

# cur.execute('SELECT * FROM campusx.std')

# for i in cur:
#  print(i)
# cur.execute("DROP TABLE IF EXISTS campusx.std")
# cur.execute("""CREATE TABLE campusx.std(
    # user_id INTEGER NOT NULL,
    # name VARCHAR(255) NOT NULL,
    # email VARCHAR(255) NOT NULL UNIQUE,
    # password VARCHAR(255) NOT NULL        
# )""")


#cur.execute('INSERT INTO campusx.std values(1,"vinay","vinay","SDFDF"),(2,"niraj","vinay001","swfs")')
#cur.execute("DROP TABLE campusx.vinay")
cur.execute("""CREATE TABLE campusx.vinay(
    user_id INTEGER NOT NULL,
    name  INTEGER NOT NULL,
    age INTEGER NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
            
    CONSTRAINT vinay_email_name_userid UNIQUE(email,name,user_id),
    CONSTRAINT vinay_userid_name  PRIMARY KEY(user_id,name)
)""")

cur.execute("""CREATE TABLE campusx.niraj(
            user_id INTEGER PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INTEGER NOT NULL,
            password VARCHAR(255) NOT NULL,
            CONSTRAINT niraj_name_email UNIQUE(name,email),
            CONSTRAINT vinay_userid AUTO_INCREMENT(user_id),
            CONSTRAINT std_check_age CHECK(age>6 AND age<25)
)""")

cur.execute("""CREATE TABLE campusx.hi(
            ticket_id INTEGER PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            travel_date DATETIME DEFAULT CURRENT_TIMESTAMP

)

""")


cur.execute("""CREATE TABLE campusx.customer(
            cid INTEGER PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE
)

""")

cur.execute("""CREATE TABLE campusx.company(
            order_id VARCHAR(255) PRIMARY KEY,
            cid INTEGER NOT NULL,
            date_time DATETIME DEFAULT CURRENT_TIMESTAMP,  
            CONSTRAINT order_id FOREIGN KEY (cid) REFERENCE campusx.customer(cid)         
)
""")


cur.execute("""CREATE TABLE campusx.customer2(
            cid INTEGER PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE
)

""")

cur.execute("""CREATE TABLE campusx.company2(
            order_id VARCHAR(255) PRIMARY KEY,
            cid INTEGER NOT NULL,
            date_time DATETIME DEFAULT CURRENT_TIMESTAMP,  
            CONSTRAINT order_id FOREIGN KEY (cid) REFERENCE campusx.customer2(cid)         
            ON DELETE CASCADE
            ON UPDATE CASCADE
            
            )           
""")
cur.execute("""(
            ALTER TABLE campusx.customer2 ADD COLUMN password VARCHAR(255)
)
""")

cur.execute("""(
            ALTER TABLE campusx.customer2 ADD COLUMN password2 VARCHAR(255) NOT NULL AFTER name
)
""")

cur.execute("""(
            ALTER TABLE campusx.customer2 
            ADD COLUMN pan_num VARCHAR(255) AFTER password2,
            ADD COLUMN joning_date VARCHAR(255) NOT NULL DEFAULT CURRENT_TIMESTAMP AFTER password
)
""")


cur.execute("""(
            ALTER TABLE campusx.customer2 
            DROP COLUMN password2,
            DROP COLUMN joing_date
)
""")

cur.execute("""ALTER TABLE campusx.customer2
            MODIFY COLUMN surname INTEGER
            
            )""")