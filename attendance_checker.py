import sqlite3

conn = sqlite3.connect('attendance_checker.db')

print ("Opened database successfully")

conn.execute('''CREATE TABLE STUDENT
         (ID INT PRIMARY KEY     NOT NULL,
         BARCODE           TEXT    NOT NULL,
         FIRST_NAME        TEXT    NOT NULL,
         MIDDLE_NAME       TEXT    NOT NULL,
         LAST_NAME         TEXT    NOT NULL,
         COURSEID                  NOT NULL,
         YEARLEVELID               NOT NULL);''')
         
print ("Table created successfully")

conn.close()

