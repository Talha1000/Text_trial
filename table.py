import mysql.connector

conn = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='people_db'
)
print("Database Connected.")

mycursor = conn.cursor()

mycursor.execute(
    "create table people (id int auto_increment primary key, user_id varchar(255), first_name varchar(255), last_name varchar(255), gender varchar(255), email varchar(255), dob date)"
)

conn.commit()
print("\nTable Created.")
