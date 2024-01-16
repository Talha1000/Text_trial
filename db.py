import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode

conn = connection.MySQLConnection(
    user='root',
    password='',
    host='localhost',
    database='trial_db'
)

conn.commit()
print("Database Connected.")

conn.close()
