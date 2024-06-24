# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newloginWrWjis.ui'
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


class New_Login(object):
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
        self.welcome.setGeometry(QRect(170, 40, 191, 51))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.welcome.setFont(font)
        self.welcome.setStyleSheet(u"color: rgb(177, 3, 3);")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(30, 210, 441, 341))
        self.labelEmail = QLabel(self.widget_3)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setGeometry(QRect(40, 30, 55, 16))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.labelEmail.setFont(font1)
        self.labelEmail.setStyleSheet(u"color: rgb(177, 3, 3);")
        self.btnLogin = QPushButton(self.widget_3)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(160, 270, 121, 41))
        self.btnLogin.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLogin.setStyleSheet(u"background-color: rgb(177, 3, 3);\n"
"color: white;\n"
"font-size: 20px;\n"
"border-radius: 5px;")
        self.labelPass = QLabel(self.widget_3)
        self.labelPass.setObjectName(u"labelPass")
        self.labelPass.setGeometry(QRect(40, 130, 91, 16))
        self.labelPass.setFont(font1)
        self.labelPass.setStyleSheet(u"color: rgb(177, 3, 3);")
        self.inputPass = QLineEdit(self.widget_3)
        self.inputPass.setObjectName(u"inputPass")
        self.inputPass.setGeometry(QRect(40, 160, 361, 41))
        self.inputPass.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;")
        self.inputPass.setEchoMode(QLineEdit.Password)
        self.inputEmail = QLineEdit(self.widget_3)
        self.inputEmail.setObjectName(u"inputEmail")
        self.inputEmail.setGeometry(QRect(40, 60, 361, 41))
        self.inputEmail.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;")
        self.error = QLabel(self.widget_3)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(120, 230, 181, 16))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.error.setFont(font2)
        self.error.setStyleSheet(u"")
        self.error.setAlignment(Qt.AlignCenter)
        self.viewschedbtn = QPushButton(self.widget_2)
        self.viewschedbtn.setObjectName(u"viewschedbtn")
        self.viewschedbtn.setGeometry(QRect(250, 180, 151, 28))
        font3 = QFont()
        self.viewschedbtn.setFont(font3)
        self.viewschedbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.viewschedbtn.setStyleSheet(u"#viewschedbtn{\n"
"	background-color: #ECE6E6;\n"
"	border: 1px solid  #B10303;\n"
"	font-size: 20px;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"#viewschedbtn:hover{\n"
"	background-color: rgb(177, 3, 3);\n"
"	color: white;\n"
"}\n"
"")
        self.loginstaffbtn = QPushButton(self.widget_2)
        self.loginstaffbtn.setObjectName(u"loginstaffbtn")
        self.loginstaffbtn.setGeometry(QRect(100, 180, 151, 28))
        self.loginstaffbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginstaffbtn.setStyleSheet(u"#loginstaffbtn{\n"
"	background-color: rgb(177, 3, 3);\n"
"	color: white;\n"
"	font-size: 20px;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"#loginstaffbtn:hover{\n"
"	color: black;\n"
"}")

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.logo.setText("")
        self.welcome.setText(QCoreApplication.translate("Form", u"Welcome", None))
        self.labelEmail.setText(QCoreApplication.translate("Form", u"Email", None))
        self.btnLogin.setText(QCoreApplication.translate("Form", u"Login", None))
        self.labelPass.setText(QCoreApplication.translate("Form", u"Password", None))
        self.error.setText("")
        self.viewschedbtn.setText(QCoreApplication.translate("Form", u"View Schedule", None))
        self.loginstaffbtn.setText(QCoreApplication.translate("Form", u"Staff Login", None))
    # retranslateUi

