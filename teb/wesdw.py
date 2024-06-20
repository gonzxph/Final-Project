from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QWidget, QLabel, QScrollArea, QVBoxLayout, QDialog
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import QtGui
import sys
import psycopg2
from ui_addscheduledialog import AddScheduleDialog
from ui_editscheduledialog import EditSchedDialog

first = [1, 2, 0, 1, 1, 2, 0, 1, 1,2,1,1,0]
last = [7, 5, 4, 9, 12, 5, 0, 9, 12,9,2,12,12]
name = ['Juan Juan', "Jack Jack", "Joe Joe", "Jeff Jeff", "James James", "Jeff Jeff", "James James", "Jeff Jeff",
        "James James","BATO","asda","Motherfucker","Kenneth Cortes"]
yes1 = []
yes2 = []
connection = psycopg2.connect(host='localhost', dbname='insurgent_db', user='postgres', password='admin', port='5432')
cursor = connection.cursor()

redframes = []  # List to store ClickableFrame instances
redframesx = []
v = .05
count = 0
timelabels = []
guidelines = []
namez = []
labelz = []
guide = []
content_height = 0

class ClickableFrame(QFrame):
    doubleClicked = pyqtSignal()  # Define doubleClicked signal using pyqtSignal

    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit()
class widgets(QFrame):
    def __init__(self, date, parent=None):
        super().__init__(parent)
        self.date = date

        self.schedScrollArea = QScrollArea(self)
        self.schedScrollArea.setGeometry(0, int(self.height() * .05), int(self.width() * .99), int(self.height() * .95))

        self.schedFrame = QFrame()
        self.schedLayout = QVBoxLayout(self.schedFrame)
        self.schedScrollArea.setWidgetResizable(True)
        self.schedScrollArea.setWidget(self.schedFrame)

        self.time = QFrame(self)
        self.time.setGeometry(int(self.width() * .9), 0, int(self.width() * .99), int(self.height() * .05))
        self.time.setStyleSheet("background-color: red")

        x = 15
        gx =0
        for a in range(10, 23):
            if a <= 12:
                tme = str(a) + " am"
            else:
                tme = str(a - 12) + " pm"
            timelabel = QLabel(tme, self.time)
            timelabel.setGeometry(x, 12, 62, 25)
            timelabels.append(timelabel)
            guideline = QFrame(self.time)
            guideline.setGeometry(gx+61,0,3,50)
            guideline.setStyleSheet("background-color:black;")
            guidelines.append(guideline)
            x += 61
            gx += 61
        self.name()

        
        
    def sched(self):
        global first, last, v, count, name,redframes,redframesx,guide,yes1,yes2,content_height
        count2 = 0
        content_height = 0
        redframes = [] 

        
        gx = 0.06
        for a in range(13):
            guideline2 = QFrame(self.schedFrame)
            guideline2.setGeometry(int((self.schedFrame.width()*gx)+(self.schedFrame.width()*.20)), 0, int(self.schedFrame.width()*.005), int(self.schedFrame.height()*.99))
            guideline2.setStyleSheet("background-color: black")
            guide.append(guideline2)
            gx += 0.06

        cursor.execute("""
            SELECT 
                employees.employee_id, 
                first_name, 
                last_name, 
                start_time, 
                end_time, 
                status,
                schedule_id
                
            FROM 
                employees 
            RIGHT JOIN 
                schedules
            ON 
                employees.employee_id = schedules.employee_id 
            WHERE 
                shift_date = '""" + self.date + """'
            ORDER BY 
                CASE status 
                    WHEN 'Regular' THEN 1
                    WHEN 'Reserve' THEN 2
                    WHEN 'Day off' THEN 3
                    ELSE 4
                END,
                start_time
        """)

        employee = cursor.fetchall()
        
        for eID,fName,lName,sTime,eTime,status, schedule_id in employee:
            if status == "Regular":
                
                redframe = ClickableFrame(self.schedFrame)
                
                redframe.setStyleSheet("background-color: #1B9620;")
                redframe.setObjectName("redframe")  # Set object name for identification

                label = QLabel("Schedule", redframe)
                label.setGeometry(10, 10, 150, 30)

                # Connect the doubleClicked signal of redframe to open_dialog method with name[count] as argument
                yes1.append(sTime-10)
                yes2.append((eTime + 12)-sTime)
                redframes.append(redframe)  # Add redframe to the list
                namez = name[count]
                redframes[count2].doubleClicked.connect(lambda emp_id=eID, emp_name=fName+" "+lName, date=self.date: self.open_update_dialog(emp_id,emp_name,date,sTime,eTime,status, schedule_id))
                count2 += 1
                
            elif status == "Reserve":
                redframex = QFrame(self.schedFrame)
               
                redframex.setStyleSheet("background-color: blue;")

                label = QLabel("Schedule", redframex)
                label.setGeometry(10, 10, 150, 30)

                redframesx.append(redframex)
            elif status == "Day off":
                redframex = QFrame(self.schedFrame)
               
                redframex.setStyleSheet("background-color: grey;")

                label = QLabel("Schedule", redframex)
                label.setGeometry(10, 10, 150, 30)

                redframesx.append(redframex)

            v += 100
            count += 1
            content_height += 100
        self.schedFrame.setMinimumHeight(content_height)

    def name(self):
        global name,namez,labelz
        
        v = 0
        namez = []
        labelz = []

        for i in reversed(range(self.schedFrame.layout().count())):
            item = self.schedFrame.layout().itemAt(i)
            item.widget().setParent(None)
            del item
        cursor.execute("""
            SELECT 
                employees.employee_id, 
                first_name, 
                last_name
            FROM 
                employees 
            left JOIN 
                schedules 
            ON 
                employees.employee_id = schedules.employee_id 
			WHERE 
    			(schedules.shift_date = '""" + self.date + """'  OR schedules.shift_date IS NULL)
            ORDER BY 
                CASE status 
                    WHEN 'Regular' THEN 1
                    WHEN 'Reserve' THEN 2
                    WHEN 'Day off' THEN 3
                    ELSE 4
                END,
                start_time
        """)

        employee = cursor.fetchall()
        count = 0
        for eID,Fname,Lname in employee:
            names = ClickableFrame(self.schedFrame)
            label = QLabel(Fname+" "+Lname, names)
            names.setGeometry(0, int(self.height()*v), int(self.width()*.20), int(self.width()*.10))
            
            # names.setStyleSheet("background-color: maroon;")
            names.setStyleSheet("""
            background-color: maroon;
            border: 5px solid #000000;  /* Black border of 2 pixels */
            border-radius: 10px;  /* Optional: rounded corners */
        """)
            label.setStyleSheet("border: none;")
            label.setGeometry( int(names.width()*.20), 20, 180, 25)
            
            names.setLineWidth(2)
            font = QtGui.QFont()
            font.setPointSize(20)  # Change 12 to your desired font size
            label.setFont(font)
            namez.append(names)
            namez[count].doubleClicked.connect(lambda emp_id=eID, emp_name=Fname+" "+Lname, date=self.date: self.open_add_schedule_dialog(emp_id, emp_name, date))

            labelz.append(label)
            v += 9.9
            count +=1
        self.sched()

    def resizeEvent(self, event):
        global timelabels,guidelines,name,namez,labelz,guide,v,first,last,redframesx,yes1,yes2,content_height
        count =0
        g = 0.06
        x = .02
        self.time.setGeometry(0, 0,int(self.width()*1) , int(self.height()*.05))
        self.schedScrollArea.setGeometry(0, int(self.height()*.04), int(self.width()*1), int(self.height()*.95))
        cursor.execute("""SELECT 
                count(employees.employee_id)
            FROM 
                employees 
            left JOIN 
                schedules 
            ON 
                employees.employee_id = schedules.employee_id 
			WHERE 
    			(schedules.shift_date = '""" + self.date + """'  OR schedules.shift_date IS NULL)""")
        emp_count = cursor.fetchall()
        print(emp_count)
        print(len(namez))
        for a in range(13):
            guidelines[a].setGeometry(((int(self.time.width()*g)+int(self.time.width()*.2))+2),0 , int(self.time.width()*.007), int(self.time.height()))
            timelabels[a].setGeometry(((int(self.time.width()*x)+int(self.time.width()*.2))),0 , int(self.time.width()*.99), int(self.time.height()))
            
            g+= 0.06
            x += .06
        v = .01
        
        for a in range(int(emp_count[0][0])):
            namez[a].setGeometry(0, int(self.schedScrollArea.height()*v), int(self.schedScrollArea.width()*.20), int(self.schedScrollArea.height()*.20))
            labelz[a].setGeometry( int(namez[a].width()*.01), 20, int(namez[a].width()*.99), 25)
            # namez[a].hide()
        
            v += .202

        v = 0.06
        count = 0
        count2 = 0
        print(len(redframesx))
        cursor.execute("""
            SELECT 
                status 
            FROM 
                schedules 
            WHERE 
                shift_date = '""" + self.date + """' 
            ORDER BY 
                CASE status 
                    WHEN 'Regular' THEN 1
                    WHEN 'Reserve' THEN 2
                    WHEN 'Day off' THEN 3
                    ELSE 4
                END,
                start_time
        """)    
        employee = cursor.fetchall()
        for status in employee:
            print(status)
            if status[0] == "Regular":
                print("count",count)
                redframes[count].setGeometry((int(self.schedScrollArea.width()*.201) + ( int((self.schedScrollArea.width())*.06)*yes1[count])), 
                                         (int(self.schedScrollArea.height()*v)),
                                         int(((self.schedScrollArea.width())*.0605)*(yes2[count]+1)), 
                                         int(self.schedScrollArea.height()*.10))
                
                count += 1

            else:
                print("count2",count2)

                redframesx[count2].setGeometry(int(self.schedScrollArea.width()*.201), 
                                               (int(self.schedScrollArea.height()*v)),
                                                int((self.schedScrollArea.width())), 
                                                int(self.schedScrollArea.height()*.10))
                
                count2 += 1 

            #     redframes[count].setGeometry(int(self.schedScrollArea.width()*.201), (int(self.schedScrollArea.height()*v)), 61 * int(self.schedScrollArea.width()*.6), int(self.schedScrollArea.width()*.10))
            

                #label.setGeometry(10, 10, 150, 30)

            v += 0.20
            content_height += v
        self.schedFrame.setMinimumHeight(int(self.schedScrollArea.height()*(.205*int(emp_count[0][0]))))

        gx = 0.06
        for a in range(13):
            guide[a].setGeometry(int((self.schedScrollArea.width()*gx)+(self.schedScrollArea.width()*.201)), 0, int(self.schedScrollArea.width()*.005), int(self.schedFrame.height()*1))
            gx += 0.06

        
        # for a in redframesx:
        #     redframesx[count].setGeometry(int(self.schedScrollArea.width()*.201), 
        #                                   (int(self.schedScrollArea.height()*v)),
        #                                     13 * int(self.schedScrollArea.width()*.06), 
        #                                   int(self.schedScrollArea.width()*.10))
        #     v += 0.10
           
        #     count += 1

        # self.label.setText(str(self.height())+
        #                    str(self.width()))
        # self.label.setGeometry(int(self.width() * 0.21), int(self.height() * 0.21),
        #                         int(self.width() * 0.58), int(self.height() * 0.58))
        # print(int(self.width()), int(self.height()),
        #                         int(self.width() ), int(self.height() ))
        # # self.repaint()

    def open_update_dialog(self, emp_id,emp_name,date,sTime,eTime,status, schedule_id):
        self.edit_schedule_dialog = QDialog()
        self.ui = EditSchedDialog(self.edit_schedule_dialog)
        self.ui.setupUi(self.edit_schedule_dialog)
        
        self.ui.emp_id.setText(str(emp_id))
        self.ui.sched_id.setText(str(schedule_id))
        self.ui.dateinput.setText(date)
        self.ui.nameinput.setText(emp_name)
        # Ensure sTime and eTime are strings
        sTime = str(sTime)
        eTime = str(eTime)

        # Set sTime in the combobox
        sTimeIndex = self.ui.frominput.findText(sTime, Qt.MatchFixedString)
        if sTimeIndex >= 0:
            self.ui.frominput.setCurrentIndex(sTimeIndex)

        # Set eTime in the combobox
        eTimeIndex = self.ui.toinput.findText(eTime, Qt.MatchFixedString)
        if eTimeIndex >= 0:
            self.ui.toinput.setCurrentIndex(eTimeIndex)
            
        statusIndex = self.ui.comboBox.findText(status, Qt.MatchFixedString)
        if statusIndex >= 0:
            self.ui.comboBox.setCurrentIndex(statusIndex)
        
        
        self.edit_schedule_dialog.show()
        
    def open_add_schedule_dialog(self, emp_id, emp_name, date):
        
        # Create an instance of the add staff dialog
        self.add_schedule_dialog = QDialog()
        self.ui = AddScheduleDialog(self.add_schedule_dialog)
        self.ui.setupUi(self.add_schedule_dialog)

        # Connect any signals or slots as needed
        self.ui.nameinput.setText(emp_name)
        self.ui.dateinput.setText(date)
        self.ui.emp_id.setText(str(emp_id))

        # Show the dialog
        self.add_schedule_dialog.show()
        
        

