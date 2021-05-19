import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

import sqlite3


qtCreatorFile = "create_student_record.ui" 

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.insert_student_button.clicked.connect(self.InsertStudentRecord)

    def InsertStudentRecord(self):
    
        first_name = self.ui.first_name_box.toPlainText()
        middle_name = self.ui.middle_name_box.toPlainText()
        last_name = self.ui.last_name_box.toPlainText()
        year_level = self.ui.year_level_box.toPlainText()
        course = self.ui.course_box.toPlainText()
        
        self.ui.first_name_box.setText("")
        self.ui.middle_name_box.setText("")
        self.ui.last_name_box.setText("")
        self.ui.year_level_box.setText("")
        self.ui.course_box.setText("")
        
        sql_command = """INSERT INTO STUDENT (ID, COURSE_ID, BARCODE, FIRST_NAME, MIDDLE_NAME, LAST_NAME, YEARLEVEL_ID) 
                             VALUES (1, '%s', 'BRCD1', '%s', '%s', '%s', '%s')""" %(course, first_name, middle_name, last_name, year_level)   
        
        #print (sql_command)   
        ##self.ui.results_window.setText(sql_command)   
        
        conn = sqlite3.connect('attendance_checker.db')
        
        conn.execute(sql_command);
         
        conn.commit()
        conn.close()
                
               
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    
    
