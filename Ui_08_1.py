# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jjyao/python_files/gui/test/08_1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog1(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 620)
        Dialog.setStyleSheet("background-color:rgb(54, 54, 54)")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 60, 191, 61))
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
        self.lineEdit__ = QtWidgets.QLineEdit(Dialog)
        self.lineEdit__.setGeometry(QtCore.QRect(190, 150, 211, 51))
        self.lineEdit__.setStyleSheet("font-size:14pt;color:rgb(255, 255, 255);\n"
"")
        self.lineEdit__.setObjectName("lineEdit__")
        self.lineEdit__2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit__2.setGeometry(QtCore.QRect(190, 250, 211, 51))
        self.lineEdit__2.setStyleSheet("font-size:14pt;color:rgb(225,225,225);")
        self.lineEdit__2.setObjectName("lineEdit__2")
        self.pushButton__ = QtWidgets.QPushButton(Dialog)
        self.pushButton__.setGeometry(QtCore.QRect(280, 420, 106, 41))
        self.pushButton__.setStyleSheet("color: rgb(35, 182, 45);font-size:15pt;\n"
"background-color: rgb(186, 189, 182);")
        self.pushButton__.setObjectName("pushButton__")
        self.lineEdit__3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit__3.setGeometry(QtCore.QRect(190, 350, 211, 51))
        self.lineEdit__3.setStyleSheet("font-size:14pt;color:rgb(225,225,225);")
        self.lineEdit__3.setObjectName("lineEdit__3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 360, 151, 21))
        self.label_4.setStyleSheet("font-size:15pt;color:rgb(35, 182, 45)")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Sign Up"))
        self.label_2.setText(_translate("Dialog", "Username"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.pushButton__.setText(_translate("Dialog", "Sign up"))
        self.label_4.setText(_translate("Dialog", "Confirm Pass"))



