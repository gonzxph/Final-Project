# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addschedulepfahJn.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1438, 791)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 301, 791))
        self.widget.setStyleSheet(u"background-color: rgb(40, 38, 38);")
        self.widgetImg = QWidget(self.widget)
        self.widgetImg.setObjectName(u"widgetImg")
        self.widgetImg.setGeometry(QRect(60, 10, 211, 101))
        self.img = QPushButton(self.widgetImg)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(0, 10, 181, 81))
        self.img.setStyleSheet(u"border-radius: 1px;")
        icon = QIcon()
        icon.addFile(u"image/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.img.setIcon(icon)
        self.img.setIconSize(QSize(200, 200))
        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(300, 0, 1141, 801))
        self.widget_2.setMinimumSize(QSize(1141, 801))
        self.widget_2.setMaximumSize(QSize(1141, 801))
        self.widget_2.setStyleSheet(u"background-color: rgb(199, 194, 194);")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 0, 1141, 101))
        self.widget_3.setStyleSheet(u"background-color: rgb(40, 38, 38);")
        self.btnaddsched = QPushButton(self.widget_3)
        self.btnaddsched.setObjectName(u"btnaddsched")
        self.btnaddsched.setGeometry(QRect(910, 40, 201, 41))
        font = QFont()
        font.setPointSize(10)
        self.btnaddsched.setFont(font)
        self.btnaddsched.setStyleSheet(u"QPushButton{\n"
"	background-color: #282626;\n"
"	color: white;\n"
"	border-radius: 5px;\n"
"	border: 1px solid white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #B10303\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icon/Add properties.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnaddsched.setIcon(icon1)
        self.btnaddsched.setIconSize(QSize(30, 30))
        self.btneditsched = QPushButton(self.widget_3)
        self.btneditsched.setObjectName(u"btneditsched")
        self.btneditsched.setGeometry(QRect(660, 40, 201, 41))
        self.btneditsched.setFont(font)
        self.btneditsched.setStyleSheet(u"QPushButton{\n"
"	background-color: #282626;\n"
"	color: white;\n"
"	border-radius: 5px;\n"
"	border: 1px solid white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #B10303\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icon/Edit Property.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btneditsched.setIcon(icon2)
        self.btneditsched.setIconSize(QSize(30, 30))
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(0, 100, 1131, 91))
        self.gridLayout = QGridLayout(self.widget_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"background-color: rgb(210, 66, 66);")
        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 41, 16))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget_5, 0, 0, 1, 1)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"background-color: rgb(204, 124, 124);")
        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 41, 16))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget_6, 0, 1, 1, 1)

        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"background-color: rgb(210, 66, 66);")
        self.label_3 = QLabel(self.widget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 20, 41, 16))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget_7, 0, 2, 1, 1)

        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"background-color: rgb(204, 124, 124);")
        self.label_4 = QLabel(self.widget_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 20, 41, 16))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget_8, 0, 3, 1, 1)

        self.widget_9 = QWidget(self.widget_4)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"background-color: rgb(210, 66, 66);\n"
"")
        self.label_5 = QLabel(self.widget_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 20, 41, 16))
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget_9, 0, 4, 1, 1)

        self.widget_10 = QWidget(self.widget_4)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"background-color: rgb(204, 124, 124);")
        self.label_6 = QLabel(self.widget_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 20, 41, 16))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget_10, 0, 5, 1, 1)

        self.widget_11 = QWidget(self.widget_4)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setStyleSheet(u"background-color: rgb(210, 66, 66);")
        self.label_7 = QLabel(self.widget_11)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 20, 41, 16))
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget_11, 0, 6, 1, 1)

        self.widget_12 = QWidget(self.widget_4)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setStyleSheet(u"background-color: rgb(204, 124, 124);")
        self.label_8 = QLabel(self.widget_12)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 20, 41, 16))
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget_12, 0, 7, 1, 1)

        self.widget_13 = QWidget(self.widget_4)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setStyleSheet(u"background-color: rgb(210, 66, 66);")
        self.label_9 = QLabel(self.widget_13)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 20, 41, 16))
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget_13, 0, 8, 1, 1)

        self.widget_14 = QWidget(self.widget_4)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setStyleSheet(u"background-color: rgb(204, 124, 124);")
        self.label_10 = QLabel(self.widget_14)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 20, 41, 16))
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget_14, 0, 9, 1, 1)

        self.widget_15 = QWidget(self.widget_4)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setStyleSheet(u"background-color: rgb(210, 66, 66);")
        self.label_11 = QLabel(self.widget_15)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 20, 41, 16))
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget_15, 0, 10, 1, 1)

        self.widget_16 = QWidget(self.widget_4)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setStyleSheet(u"background-color: rgb(204, 124, 124);")
        self.label_12 = QLabel(self.widget_16)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 20, 41, 16))
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget_16, 0, 11, 1, 1)

        self.widget_17 = QWidget(self.widget_4)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setStyleSheet(u"background-color: rgb(210, 66, 66);")
        self.label_13 = QLabel(self.widget_17)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 20, 41, 16))
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget_17, 0, 12, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.img.setText("")
        self.btnaddsched.setText(QCoreApplication.translate("Dialog", u"   Add Schedule", None))
        self.btneditsched.setText(QCoreApplication.translate("Dialog", u"  Edit Schedule", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"10 AM", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"11 AM", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"12 PM", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"1 PM", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"2 PM", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"3 PM", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"4 PM", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"5 PM", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"6 PM", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"7 PM", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"8 PM", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"9 PM", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"10 PM", None))
    # retranslateUi

