# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jjyao/python_files/gui/test/08.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 620)
        Dialog.setStyleSheet("background-color:rgb(54, 54, 54)")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 60, 121, 61))
        self.label.setStyleSheet("color:rgb(225,225,225);font-size:28pt;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 131, 21))
        self.label_2.setStyleSheet("font-size:15pt;color:rgb(35, 182, 45);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 260, 131, 21))
        self.label_3.setStyleSheet("font-size:15pt;color:rgb(35, 182, 45)")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 150, 231, 51))
        self.lineEdit.setStyleSheet("font-size:14pt;color:rgb(255, 255, 255);\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 250, 231, 51))
        self.lineEdit_2.setStyleSheet("font-size:14pt;color:rgb(225,225,225);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 420, 106, 41))
        self.pushButton.setStyleSheet("color: rgb(35, 182, 45);font-size:15pt;\n"
"background-color: rgb(186, 189, 182);")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, 360, 261, 21))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 360, 191, 31))
        self.pushButton_2.setStyleSheet("color: rgb(35, 182, 45);font-size:12pt;\n"
"background-color: rgb(186, 189, 182);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Login"))
        self.label_2.setText(_translate("Dialog", "Username"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.pushButton.setText(_translate("Dialog", "login"))
        self.label_4.setText(_translate("Dialog", "还没有账户吗？点击注册按钮"))
        self.pushButton_2.setText(_translate("Dialog", "Create Account"))




