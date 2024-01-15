import mysql.connector
from mysql.connector import errorcode

db = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='trial_db'
)

mycursor = db.cursor()

mycursor.execute(
    "create table people (Serial int auto_increment primary key, NID varchar(255), first_name varchar(255), last_name varchar(255), gender varchar(255), email varchar(255), Date_of_Birth date)"
)

db.commit()
