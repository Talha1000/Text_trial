import mysql.connector

i = 0


def insert_data_from_text_file(filename, cursor, connection):
    with open(filename, 'r') as file:
        global i
        for line in file:
            data = line.strip().split(' | ')
            if len(data) != 6:
                print(
                    f"Error: Expected 6 values, but got {len(data)} values in line: {line}")
                continue
            else:
                i += 1
                print([i], data[2], data[3] + "\t[Data Recorded]")

            query = "insert into people(user_id, first_name, last_name, gender, email, dob) values (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, tuple(data))


conn = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='people_db'
)

mycursor = conn.cursor()

insert_data_from_text_file('peoples.txt', mycursor, conn)

conn.commit()
print("\nData Record Successful.")

mycursor.close()
conn.close()
