# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'staff1KikyYt.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


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
        icon.addFile(u"../image/Logo1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(200, 200))
        self.pushButton.setCheckable(True)

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_2 = QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.staffbtn = QPushButton(self.widget_4)
        self.staffbtn.setObjectName(u"staffbtn")
        self.staffbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.staffbtn.setStyleSheet(u"#staffbtn{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"margin: 0 40px;\n"
"padding: 7px;\n"
"color: white;\n"
"background-color: #B10303;\n"
"}\n"
"\n"
"#staffbtn:hover{\n"
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

        self.kioskbtn = QPushButton(self.widget_4)
        self.kioskbtn.setObjectName(u"kioskbtn")
        self.kioskbtn.setStyleSheet(u"#kioskbtn{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"margin: 0 40px;\n"
"padding: 7px;\n"
"color: white;\n"
"}\n"
"\n"
"#kioskbtn:hover{\n"
"	background-color: #B10303;\n"
"	color: black;\n"
"}")

        self.gridLayout_2.addWidget(self.kioskbtn, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_3 = QGridLayout(self.widget_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.verticalLayout.addWidget(self.widget_5)

        self.widget_L2 = QWidget(self.widget)
        self.widget_L2.setObjectName(u"widget_L2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_L2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_L = QWidget(self.widget_L2)
        self.widget_L.setObjectName(u"widget_L")

        self.verticalLayout_3.addWidget(self.widget_L)

        self.widget_L1 = QWidget(self.widget_L2)
        self.widget_L1.setObjectName(u"widget_L1")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_L1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.logoutbtn = QPushButton(self.widget_L1)
        self.logoutbtn.setObjectName(u"logoutbtn")
        self.logoutbtn.setStyleSheet(u"#logoutbtn{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"margin: 0 40px;\n"
"padding: 7px;\n"
"color: white;\n"
"}\n"
"\n"
"#logoutbtn:hover{\n"
"	background-color: #B10303;\n"
"	color: black;\n"
"}")

        self.horizontalLayout_7.addWidget(self.logoutbtn)


        self.verticalLayout_3.addWidget(self.widget_L1)


        self.verticalLayout.addWidget(self.widget_L2)


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
        self.horizontalLayout_3 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_13 = QWidget(self.widget_7)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.branchname = QWidget(self.widget_13)
        self.branchname.setObjectName(u"branchname")

        self.horizontalLayout_4.addWidget(self.branchname)


        self.horizontalLayout_3.addWidget(self.widget_13)

        self.widget_12 = QWidget(self.widget_7)
        self.widget_12.setObjectName(u"widget_12")

        self.horizontalLayout_3.addWidget(self.widget_12)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)

        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget_9 = QWidget(self.widget_2)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"background-color: rgb(236, 230, 230);")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")

        self.horizontalLayout_2.addWidget(self.widget_10)

        self.widget_14 = QWidget(self.widget_9)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.deletestaffbtn = QPushButton(self.widget_14)
        self.deletestaffbtn.setObjectName(u"deletestaffbtn")
        self.deletestaffbtn.setStyleSheet(u"#deletestaffbtn{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"margin: 0 5px;\n"
"padding: 7px;\n"
"background-color: #B10303;\n"
"color: white;\n"
"}\n"
"\n"
"#deletestaffbtn:hover{\n"
"	color: black;\n"
"}")

        self.horizontalLayout_5.addWidget(self.deletestaffbtn)


        self.horizontalLayout_2.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.widget_9)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.updatestaffbtn = QPushButton(self.widget_15)
        self.updatestaffbtn.setObjectName(u"updatestaffbtn")
        self.updatestaffbtn.setStyleSheet(u"#updatestaffbtn{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"margin: 0 5px;\n"
"padding: 7px;\n"
"background-color: #B10303;\n"
"color: white;\n"
"}\n"
"\n"
"#updatestaffbtn:hover{\n"
"	color: black;\n"
"}")

        self.horizontalLayout_6.addWidget(self.updatestaffbtn)


        self.horizontalLayout_2.addWidget(self.widget_15)

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

        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)

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

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText("")
        self.staffbtn.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.schedbtn.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.kioskbtn.setText(QCoreApplication.translate("MainWindow", u"KIOSK", None))
        self.logoutbtn.setText(QCoreApplication.translate("MainWindow", u"LOGOUT", None))
        self.deletestaffbtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.updatestaffbtn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.addstaffbtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
    # retranslateUi

