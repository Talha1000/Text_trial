from mysql.connector import (connection)

conn = connection.MySQLConnection(
    user='root',
    password='',
    host='localhost',
)

mycursor = conn.cursor()

mycursor.execute("create database people_db")

conn.commit()
print("Database Created.")

conn.close()
