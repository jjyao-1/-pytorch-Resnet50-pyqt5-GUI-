# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jjyao/python_files/gui/maincode/work.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton___ = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton___.setGeometry(QtCore.QRect(370, 390, 106, 30))
        self.pushButton___.setObjectName("pushButton___")
        self.label___2 = QtWidgets.QLabel(self.centralwidget)
        self.label___2.setGeometry(QtCore.QRect(340, 160, 90, 27))
        self.label___2.setObjectName("label___2")
        self.lineEdit___ = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit___.setGeometry(QtCore.QRect(510, 160, 159, 29))
        self.lineEdit___.setText("")
        self.lineEdit___.setObjectName("lineEdit___")
        self.label___ = QtWidgets.QLabel(self.centralwidget)
        self.label___.setGeometry(QtCore.QRect(50, 70, 224, 224))
        self.label___.setStyleSheet("background-color:rgb(211, 215, 207) ;")
        self.label___.setText("")
        self.label___.setObjectName("label___")
        self.label___3 = QtWidgets.QLabel(self.centralwidget)
        self.label___3.setGeometry(QtCore.QRect(120, 320, 90, 27))
        self.label___3.setObjectName("label___3")
        self.pushButton___2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton___2.setGeometry(QtCore.QRect(590, 390, 141, 30))
        self.pushButton___2.setObjectName("pushButton___2")
        self.label___4 = QtWidgets.QLabel(self.centralwidget)
        self.label___4.setGeometry(QtCore.QRect(0, 0, 800, 620))
        self.label___4.setText("")
        self.label___4.setObjectName("label___4")
        self.pushButton___1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton___1.setGeometry(QtCore.QRect(50, 390, 221, 30))
        self.pushButton___1.setObjectName("pushButton___1")
        self.label___4.raise_()
        self.label___2.raise_()
        self.lineEdit___.raise_()
        self.label___.raise_()
        self.pushButton___.raise_()
        self.label___3.raise_()
        self.pushButton___2.raise_()
        self.pushButton___1.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 32))
        self.menubar.setObjectName("menubar")
        self.menuFiles = QtWidgets.QMenu(self.menubar)
        self.menuFiles.setObjectName("menuFiles")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menu = QtWidgets.QMenu(self.menuSetting)
        self.menu.setObjectName("menu")
        self.menu_3 = QtWidgets.QMenu(self.menuSetting)
        self.menu_3.setObjectName("menu_3")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.actionRed = QtWidgets.QAction(MainWindow)
        self.actionRed.setObjectName("actionRed")
        self.actionGreen = QtWidgets.QAction(MainWindow)
        self.actionGreen.setObjectName("actionGreen")
        self.actionBlack = QtWidgets.QAction(MainWindow)
        self.actionBlack.setObjectName("actionBlack")
        self.actionGray = QtWidgets.QAction(MainWindow)
        self.actionGray.setObjectName("actionGray")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.actionWhite = QtWidgets.QAction(MainWindow)
        self.actionWhite.setObjectName("actionWhite")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.actionRed_2 = QtWidgets.QAction(MainWindow)
        self.actionRed_2.setObjectName("actionRed_2")
        self.actionGreen_2 = QtWidgets.QAction(MainWindow)
        self.actionGreen_2.setObjectName("actionGreen_2")
        self.actionGray_2 = QtWidgets.QAction(MainWindow)
        self.actionGray_2.setObjectName("actionGray_2")
        self.actionBlack_2 = QtWidgets.QAction(MainWindow)
        self.actionBlack_2.setObjectName("actionBlack_2")
        self.actionWhite_2 = QtWidgets.QAction(MainWindow)
        self.actionWhite_2.setObjectName("actionWhite_2")
        self.menuFiles.addAction(self.actionOpen)
        self.menuFiles.addAction(self.action)
        self.menu.addAction(self.actionRed)
        self.menu.addAction(self.actionGreen)
        self.menu.addAction(self.actionBlack)
        self.menu.addAction(self.actionGray)
        self.menu.addAction(self.actionWhite)
        self.menu_3.addSeparator()
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionRed_2)
        self.menu_3.addAction(self.actionGreen_2)
        self.menu_3.addAction(self.actionGray_2)
        self.menu_3.addAction(self.actionBlack_2)
        self.menu_3.addAction(self.actionWhite_2)
        self.menuSetting.addAction(self.menu.menuAction())
        self.menuSetting.addAction(self.action_8)
        self.menuSetting.addSeparator()
        self.menuSetting.addAction(self.menu_3.menuAction())
        self.menuHelp.addAction(self.action_4)
        self.menuHelp.addAction(self.action_5)
        self.menuHelp.addAction(self.action_6)
        self.menuHelp.addAction(self.action_7)
        self.menu_2.addAction(self.action_3)
        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton___.setText(_translate("MainWindow", "开始识别"))
        self.label___2.setText(_translate("MainWindow", "识别结果："))
        self.label___3.setText(_translate("MainWindow", "图像显示区"))
        self.pushButton___2.setText(_translate("MainWindow", "返回登录界面"))
        self.pushButton___1.setText(_translate("MainWindow", "更改图像显示区背景图片"))
        self.menuFiles.setTitle(_translate("MainWindow", "文件"))
        self.menuSetting.setTitle(_translate("MainWindow", "设置"))
        self.menu.setTitle(_translate("MainWindow", "背景"))
        self.menu_3.setTitle(_translate("MainWindow", "显示区背景颜色"))
        self.menuHelp.setTitle(_translate("MainWindow", "帮助"))
        self.menu_2.setTitle(_translate("MainWindow", "信息"))
        self.actionOpen.setText(_translate("MainWindow", "打开"))
        self.action.setText(_translate("MainWindow", "关闭"))
        self.action_2.setText(_translate("MainWindow", "退出"))
        self.action_4.setText(_translate("MainWindow", "关于软件"))
        self.action_5.setText(_translate("MainWindow", "帮助文档"))
        self.action_6.setText(_translate("MainWindow", "源代码"))
        self.actionRed.setText(_translate("MainWindow", "Red"))
        self.actionGreen.setText(_translate("MainWindow", "Green"))
        self.actionBlack.setText(_translate("MainWindow", "Black"))
        self.actionGray.setText(_translate("MainWindow", "Gray"))
        self.action_7.setText(_translate("MainWindow", "举报"))
        self.action_8.setText(_translate("MainWindow", "自定义背景"))
        self.actionWhite.setText(_translate("MainWindow", "White"))
        self.action_3.setText(_translate("MainWindow", "用户列表"))
        self.actionRed_2.setText(_translate("MainWindow", "Red"))
        self.actionGreen_2.setText(_translate("MainWindow", "Green"))
        self.actionGray_2.setText(_translate("MainWindow", "Gray"))
        self.actionBlack_2.setText(_translate("MainWindow", "Black"))
        self.actionWhite_2.setText(_translate("MainWindow", "White"))

