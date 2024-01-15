import mysql.connector
from mysql.connector import errorcode


def insert_data_from_text_file(filename, cursor, connection):
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(' | ')
            if len(data) != 6:
                print(
                    f"Error: Expected 6 values, but got {len(data)} values in line: {line}")
                continue

            query = "insert into people(NID, first_name, last_name, gender, email, Date_of_Birth) values (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, tuple(data))


conn = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='trial_db'
)

mycursor = conn.cursor()

insert_data_from_text_file('peoples.txt', mycursor, conn)

conn.commit()

mycursor.close()
conn.close()
