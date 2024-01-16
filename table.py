import mysql.connector
from mysql.connector import errorcode

conn = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='trial_db'
)

mycursor = conn.cursor()

mycursor.execute(
    "create table people (id int auto_increment primary key, user_id varchar(255), first_name varchar(255), last_name varchar(255), gender varchar(255), email varchar(255), dob date)"
)

conn.commit()
print("Table Created.")
