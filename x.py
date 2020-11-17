import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='251209111', database='bus_management')
cursor = conn.cursor()

cursor.execute('desc booking;')
print(cursor.fetchall())
conn.commit()
conn.close()