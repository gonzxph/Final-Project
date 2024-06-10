# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'schedulexPBebq.ui'
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
        self.btnsched = QPushButton(self.widget)
        self.btnsched.setObjectName(u"btnsched")
        self.btnsched.setGeometry(QRect(50, 220, 201, 41))
        font = QFont()
        font.setPointSize(10)
        self.btnsched.setFont(font)
        self.btnsched.setStyleSheet(u"background-color: rgb(177, 3, 3);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        icon1 = QIcon()
        icon1.addFile(u"icon/Clock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnsched.setIcon(icon1)
        self.btnsched.setIconSize(QSize(30, 30))
        self.btnstaff = QPushButton(self.widget)
        self.btnstaff.setObjectName(u"btnstaff")
        self.btnstaff.setGeometry(QRect(50, 300, 201, 41))
        self.btnstaff.setFont(font)
        self.btnstaff.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(40, 38, 38);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    border: 1px solid white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #B10303;\n"
"	border: 0px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icon/Management.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnstaff.setIcon(icon2)
        self.btnstaff.setIconSize(QSize(30, 30))
        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(300, 0, 1141, 801))
        self.widget_2.setMinimumSize(QSize(1141, 801))
        self.widget_2.setMaximumSize(QSize(1141, 801))
        self.widget_2.setStyleSheet(u"background-color: rgb(199, 194, 194);")
        self.calendarWidget = QCalendarWidget(self.widget_2)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(80, 170, 971, 491))
        self.calendarWidget.setStyleSheet(u"background-color: rgb(128, 234, 255);")
        self.btnaddsched = QPushButton(self.widget_2)
        self.btnaddsched.setObjectName(u"btnaddsched")
        self.btnaddsched.setGeometry(QRect(850, 110, 201, 41))
        self.btnaddsched.setFont(font)
        self.btnaddsched.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(40, 38, 38);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    border: 1px solid white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #B10303;\n"
"	border: 0px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icon/Add properties.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnaddsched.setIcon(icon3)
        self.btnaddsched.setIconSize(QSize(30, 30))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.img.setText("")
        self.btnsched.setText(QCoreApplication.translate("Dialog", u"   Schedule", None))
        self.btnstaff.setText(QCoreApplication.translate("Dialog", u"  Staff", None))
        self.btnaddsched.setText(QCoreApplication.translate("Dialog", u"   Add Schedule", None))
    # retranslateUi

