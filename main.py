import mysql.connector

conn = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='trial_db'
)

mycursor = conn.cursor()

mycursor.execute("SELECT * FROM people")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

conn.commit()
