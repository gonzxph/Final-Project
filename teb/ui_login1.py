# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginFzEuNd.ui'
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


class Ui_Form1(object):
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
        icon.addFile(u"image/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logo.setIcon(icon)
        self.logo.setIconSize(QSize(550, 520))

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(199, 194, 194);")
        self.welcome = QLabel(self.widget_2)
        self.welcome.setObjectName(u"welcome")
        self.welcome.setGeometry(QRect(170, 90, 191, 51))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.welcome.setFont(font)
        self.welcome.setStyleSheet(u"color: rgb(177, 3, 3);")
        self.labelEmail = QLabel(self.widget_2)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setGeometry(QRect(80, 250, 55, 16))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.labelEmail.setFont(font1)
        self.labelEmail.setStyleSheet(u"color: rgb(177, 3, 3);")
        self.inputEmail = QLineEdit(self.widget_2)
        self.inputEmail.setObjectName(u"inputEmail")
        self.inputEmail.setGeometry(QRect(80, 280, 361, 41))
        self.inputEmail.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;")
        self.labelPass = QLabel(self.widget_2)
        self.labelPass.setObjectName(u"labelPass")
        self.labelPass.setGeometry(QRect(80, 350, 91, 16))
        self.labelPass.setFont(font1)
        self.labelPass.setStyleSheet(u"color: rgb(177, 3, 3);")
        self.inputPass = QLineEdit(self.widget_2)
        self.inputPass.setObjectName(u"inputPass")
        self.inputPass.setGeometry(QRect(80, 380, 361, 41))
        self.inputPass.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;")
        self.inputPass.setEchoMode(QLineEdit.Password)
        self.btnLogin = QPushButton(self.widget_2)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(200, 490, 121, 41))
        self.btnLogin.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLogin.setStyleSheet(u"background-color: rgb(177, 3, 3);\n"
"color: white;\n"
"font-size: 20px;\n"
"border-radius: 5px;")
        self.error = QLabel(self.widget_2)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(180, 180, 181, 16))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.error.setFont(font2)

        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.logo.setText("")
        self.welcome.setText(QCoreApplication.translate("Form", u"Welcome", None))
        self.labelEmail.setText(QCoreApplication.translate("Form", u"Email", None))
        self.labelPass.setText(QCoreApplication.translate("Form", u"Password", None))
        self.btnLogin.setText(QCoreApplication.translate("Form", u"Login", None))
        self.error.setText("")
    # retranslateUi

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     Form = QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())   