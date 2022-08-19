from sqlite3 import Cursor
import mysql.connector

conn = mysql.connector.connect(host='127.0.0.1', database='lifelog', user='root', password='')
cursor = conn.cursor()

cursor.execute(
    """
    select * from sleep
    """
)

for rec in cursor:
    print(rec)

# conn.commit()

cursor.close()
conn.close()