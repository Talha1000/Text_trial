import mysql.connector
from prettytable import PrettyTable

conn = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='trial_db'
)


mycursor = conn.cursor()
mycursor.execute("SELECT * FROM people")
result = mycursor.fetchall()

columns = [desc[0] for desc in mycursor.description]

table = PrettyTable(columns)

for row in result:
    table.add_row(row)

print(table)

mycursor.close()
conn.commit()
conn.close()
