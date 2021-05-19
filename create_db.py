import sqlite3

conn = sqlite3.connect('attendance_checker.db')

print ("Opened database successfully")

conn.execute('''CREATE TABLE COURSE
         (ID INT PRIMARY KEY     NOT NULL,
         COURSE_INITIAL    TEXT    NOT NULL,
         COURSE_NAME       TEXT    NOT NULL);''')
         
conn.execute('''CREATE TABLE STUDENT
         (ID INT PRIMARY KEY       NOT NULL,
         COURSE_ID  INT            NOT NULL,
         BARCODE           TEXT    NOT NULL,
         FIRST_NAME        TEXT    NOT NULL,
         MIDDLE_NAME       TEXT    NOT NULL,
         LAST_NAME         TEXT    NOT NULL,
         YEARLEVEL_ID              NOT NULL,
         FOREIGN KEY (COURSE_ID)  REFERENCES COURSE(ID));''')
         
print ("Table created successfully")

conn.execute("""INSERT INTO COURSE (ID, COURSE_INITIAL, COURSE_NAME ) 
                            VALUES (1, 'BSCS', 'BACHELOR OF SCIENCE IN COMPUTER SCIENCE')""");

conn.execute("""INSERT INTO STUDENT (ID, COURSE_ID, BARCODE, FIRST_NAME, MIDDLE_NAME, LAST_NAME, YEARLEVEL_ID) 
                             VALUES (1, 1, 'BRCD2',  )""");
         
conn.commit()
conn.close()

print ("Initial record inserted")