import mysql.connector

conn = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='trial_db'
)

mycursor = conn.cursor()

mycursor.execute("drop table people")

conn.commit()
