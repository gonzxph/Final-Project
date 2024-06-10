# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'staff1fSXHqX.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
import psycopg2  # Import psycopg2 for PostgreSQL operations
import datetime
from PyQt5.uic import loadUi


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1497, 849)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(40, 38, 38);")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border: none;")
        icon = QIcon()
        icon.addFile(u"image/Logo1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(200, 200))

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_2 = QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.staffbtn = QPushButton(self.widget_4)
        self.staffbtn.setObjectName(u"staffbtn")
        self.staffbtn.setStyleSheet(u"#staffbtn{\n"
                                    "border: 1px solid white;\n"
                                    "border-radius: 5px;\n"
                                    "margin: 0 40px;\n"
                                    "padding: 7px;\n"
                                    "color: white;\n"
                                    "}\n"
                                    "\n"
                                    "#staffbtn:hover{\n"
                                    "	background-color: #B10303;\n"
                                    "	color: black;\n"
                                    "}")

        self.gridLayout_2.addWidget(self.staffbtn, 0, 0, 1, 1)

        self.schedbtn = QPushButton(self.widget_4)
        self.schedbtn.setObjectName(u"schedbtn")
        self.schedbtn.setStyleSheet(u"#schedbtn{\n"
                                    "border: 1px solid white;\n"
                                    "border-radius: 5px;\n"
                                    "margin: 0 40px;\n"
                                    "padding: 7px;\n"
                                    "color: white;\n"
                                    "}\n"
                                    "\n"
                                    "#schedbtn:hover{\n"
                                    "	background-color: #B10303;\n"
                                    "	color: black;\n"
                                    "}")

        self.gridLayout_2.addWidget(self.schedbtn, 1, 0, 1, 1)

        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_3 = QGridLayout(self.widget_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.verticalLayout.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")

        self.verticalLayout.addWidget(self.widget_6)

        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(236, 230, 230);")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"background-color: rgb(236, 230, 230);")

        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget_9 = QWidget(self.widget_2)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"background-color: rgb(236, 230, 230);")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")

        self.horizontalLayout_2.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_4 = QGridLayout(self.widget_11)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.addstaffbtn = QPushButton(self.widget_11)
        self.addstaffbtn.setObjectName(u"addstaffbtn")
        self.addstaffbtn.setStyleSheet(u"#addstaffbtn{\n"
                                       "border: 1px solid white;\n"
                                       "border-radius: 5px;\n"
                                       "margin: 0 5px;\n"
                                       "padding: 7px;\n"
                                       "background-color: #B10303;\n"
                                       "color: white;\n"
                                       "}\n"
                                       "\n"
                                       "#addstaffbtn:hover{\n"
                                       "	color: black;\n"
                                       "}")

        self.gridLayout_4.addWidget(self.addstaffbtn, 0, 0, 1, 1)

        self.horizontalLayout_2.addWidget(self.widget_11)

        self.horizontalLayout_2.setStretch(0, 9)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.widget_9)

        self.widget_8 = QWidget(self.widget_2)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"background-color: rgb(236, 230, 230);")
        self.gridLayout_5 = QGridLayout(self.widget_8)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.table = QWidget(self.widget_8)
        self.table.setObjectName(u"table")
        self.table.setStyleSheet(u"")
        self.gridLayout_6 = QGridLayout(self.table)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tableWidget = QTableWidget(self.table)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_6.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.gridLayout_5.addWidget(self.table, 0, 0, 1, 1)

        self.verticalLayout_2.addWidget(self.widget_8)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 10)

        self.horizontalLayout.addWidget(self.widget_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        
        
        self.addstaffbtn.clicked.connect(self.open_add_staff_dialog)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        # Load data from the database
        self.load_data()

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText("")
        self.staffbtn.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.schedbtn.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.addstaffbtn.setText(QCoreApplication.translate("MainWindow", u"Add Staff", None))

    # retranslateUi

    def load_data(self):
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(host='localhost', dbname='insurgent_db', user='postgres', password='admin',
                                port='5432')
        cursor = conn.cursor()

        # Retrieve data from the employees table
        cursor.execute('SELECT first_name, last_name, address, hire_date, phone, email FROM employees')
        rows = cursor.fetchall()

        self.tableWidget.setColumnCount(
            6)  # Set the number of columns
        self.tableWidget.setHorizontalHeaderLabels(
            ['First Name', 'Last Name', 'Address', 'Hire Date', 'Phone', 'Email'])
        self.tableWidget.setRowCount(
            len(rows))  # Set the number of rows

        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data):
                if isinstance(col_data, datetime.date):
                    col_data = col_data.strftime('%Y-%m-%d')  # Convert the date to string
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        # Close the connection
        cursor.close()
        conn.close()

    def open_add_staff_dialog(self):
        # Create an instance of the add staff dialog
        self.add_staff_dialog = QDialog()
        self.add_staff_dialog_ui = loadUi("addstaff.ui", self.add_staff_dialog)

        # Connect any signals or slots as needed

        # Show the dialog
        self.add_staff_dialog.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
