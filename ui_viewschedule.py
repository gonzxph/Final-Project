# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewscheduleAuDRqT.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import datetime
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
import psycopg2

conn = psycopg2.connect(host='localhost', dbname='insurgent_db', user='postgres', password='admin', port='5432')
cursor = conn.cursor()

class View_Schedule(QWidget):
    def __init__(self, stacked_widget):
        super(View_Schedule, self).__init__()
        self.stacked_widget = stacked_widget
        self.setupUi(self)
        
        
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1006, 575)
        Form.setMinimumSize(QSize(1006, 575))
        Form.setMaximumSize(QSize(1006, 575))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setAcceptDrops(False)
        self.widget.setStyleSheet(u"background-color: rgb(40, 38, 38);")
        self.logo = QPushButton(self.widget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(0, 70, 491, 401))
        self.logo.setMinimumSize(QSize(491, 401))
        self.logo.setMaximumSize(QSize(421, 401))
        self.logo.setStyleSheet(u"border-radius: 1px;")
        icon = QIcon()
        icon.addFile(u":/image/image/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logo.setIcon(icon)
        self.logo.setIconSize(QSize(550, 520))
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(510, 0, 503, 575))
        self.widget_2.setStyleSheet(u"background-color: rgb(199, 194, 194);")
        self.welcome = QLabel(self.widget_2)
        self.welcome.setObjectName(u"welcome")
        self.welcome.setGeometry(QRect(110, 70, 301, 51))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.welcome.setFont(font)
        self.welcome.setStyleSheet(u"color: rgb(177, 3, 3);")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(30, 210, 441, 341))
        self.tableWidget = QTableWidget(self.widget_3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 90, 441, 251))
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 61, 22))
        self.startdateinput = QDateEdit(self.widget_3)
        self.startdateinput.setObjectName(u"startdateinput")
        self.startdateinput.setDisplayFormat("MM/dd/yyyy")  
        self.startdateinput.setDate(datetime.date.today())
        self.startdateinput.setDate(self.startdateinput.date().addDays(-7))
        self.startdateinput.setGeometry(QRect(80, 20, 110, 22))
        self.startdateinput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;\n"
"padding: 4px;")
        self.enddateinput = QDateEdit(self.widget_3)
        self.enddateinput.setObjectName(u"enddateinput")
        self.enddateinput.setDisplayFormat("MM/dd/yyyy")
        self.enddateinput.setDate(datetime.date.today())
        self.enddateinput.setGeometry(QRect(320, 20, 110, 22))
        self.enddateinput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;\n"
"padding: 4px;")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 20, 61, 22))
        self.searchinput = QLineEdit(self.widget_3)
        self.searchinput.setObjectName(u"searchinput")
        self.searchinput.setGeometry(QRect(130, 60, 191, 28))
        self.searchinput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;\n"
"padding: 4px;")
        self.searchbtn = QPushButton(self.widget_3)
        self.searchbtn.setObjectName(u"searchbtn")
        self.searchbtn.setGeometry(QRect(330, 60, 101, 28))
        self.searchbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchbtn.setStyleSheet(u"#searchbtn{\n"
"	background-color: rgb(177, 3, 3);\n"
"	color: white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#searchbtn:hover{\n"
"	color: black;\n"
"}")
        self.viewschedbtn = QPushButton(self.widget_2)
        self.viewschedbtn.setObjectName(u"viewschedbtn")
        self.viewschedbtn.setGeometry(QRect(250, 180, 151, 28))
        font1 = QFont()
        self.viewschedbtn.setFont(font1)
        self.viewschedbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.viewschedbtn.setStyleSheet(u"#viewschedbtn{\n"
"	background-color: rgb(177, 3, 3);\n"
"	color: white;\n"
"	font-size: 20px;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"#viewschedbtn:hover{\n"
"	color: black;\n"
"}")
        self.loginstaffbtn = QPushButton(self.widget_2)
        self.loginstaffbtn.setObjectName(u"loginstaffbtn")
        self.loginstaffbtn.setGeometry(QRect(100, 180, 151, 28))
        self.loginstaffbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginstaffbtn.setStyleSheet(u"#loginstaffbtn{\n"
"	background-color: #ECE6E6;\n"
"	border: 1px solid  #B10303;\n"
"	font-size: 20px;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"#loginstaffbtn:hover{\n"
"	background-color: rgb(177, 3, 3);\n"
"	color: white;\n"
"}")

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
        self.searchbtn.clicked.connect(self.search_staff)
        self.load_data()
        
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.logo.setText("")
        self.welcome.setText(QCoreApplication.translate("Form", u"Staff Schedules", None))
        self.label.setText(QCoreApplication.translate("Form", u"Start Date", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"End Date", None))
        self.searchinput.setPlaceholderText(QCoreApplication.translate("Form", u"Search name...", None))
        self.searchbtn.setText(QCoreApplication.translate("Form", u"Search", None))
        self.viewschedbtn.setText(QCoreApplication.translate("Form", u"View Schedule", None))
        self.loginstaffbtn.setText(QCoreApplication.translate("Form", u"Staff Login", None))
    # retranslateUi
    
    

    def load_data(self):
        # Retrieve data from the employees table including the staff ID
        start_date_obj = datetime.datetime.strptime(self.startdateinput.text(), "%m/%d/%Y")
        end_date_obj = datetime.datetime.strptime(self.enddateinput.text(), "%m/%d/%Y")

        searchinput = self.searchinput.text().lower()
        end_date = end_date_obj.strftime("%Y-%m-%d")
        start_date = start_date_obj.strftime("%Y-%m-%d")
        
        cursor.execute("""select e.employee_id, e.first_name, e.last_name, s.shift_date, s.start_time, s.end_time from schedules s natural join employees e 
                       WHERE shift_date BETWEEN %s AND %s
""", (start_date, end_date))
        rows = cursor.fetchall()
        
        

        self.tableWidget.setColumnCount(6)  # Set the number of columns including the hidden ID column
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'First Name', 'Last Name', 'Shift Date', 'Start Time', 'End Time'])
        self.tableWidget.setRowCount(len(rows))

        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data):
                if isinstance(col_data, datetime.date):
                    col_data = col_data.strftime('%Y-%m-%d')  # Convert the date to string
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        # Hide the ID column
        self.tableWidget.setColumnHidden(0, True)
        
    def search_staff(self):
        start_date_obj = datetime.datetime.strptime(self.startdateinput.text(), "%m/%d/%Y")
        end_date_obj = datetime.datetime.strptime(self.enddateinput.text(), "%m/%d/%Y")

        searchinput = self.searchinput.text().lower()
        end_date = end_date_obj.strftime("%Y-%m-%d")
        start_date = start_date_obj.strftime("%Y-%m-%d")
        
        if searchinput == "":
                cursor.execute("""select e.employee_id, e.first_name, e.last_name, s.shift_date, s.start_time, s.end_time from schedules s natural join employees e 
                       WHERE shift_date BETWEEN %s AND %s
                """, (start_date, end_date))
                rows = cursor.fetchall()
        else:
                cursor.execute("""select e.employee_id, e.first_name, e.last_name, s.shift_date, s.start_time, s.end_time from schedules s natural join employees e 
                       WHERE (shift_date BETWEEN %s AND %s) AND (lower(first_name) LIKE %s OR lower(last_name) LIKE %s)
                """, (start_date, end_date, '%'+searchinput+'%', '%'+searchinput+'%'))
                rows = cursor.fetchall()
        
        

        self.tableWidget.setColumnCount(6)  # Set the number of columns including the hidden ID column
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'First Name', 'Last Name', 'Shift Date', 'Start Time', 'End Time'])
        self.tableWidget.setRowCount(len(rows))

        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data):
                if isinstance(col_data, datetime.date):
                    col_data = col_data.strftime('%Y-%m-%d')  # Convert the date to string
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        # Hide the ID column
        self.tableWidget.setColumnHidden(0, True)