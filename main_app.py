from random import expovariate
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
#from Ui_08 import Ui_Form
from Ui_08 import Ui_Dialog
from Ui_08_1 import Ui_Dialog1
from Ui_work import Ui_MainWindow
from call_work import MyMainForm2


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QAction
from Ui_work import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl, QFileInfo
from PyQt5.QtGui import QDesktopServices


import torch
import torchvision
from torchvision import datasets, models, transforms
import os
from torch.autograd import Variable
import matplotlib.pyplot as plt
import time
from PIL import Image, ImageQt
import webbrowser

# username = 'admin'
# password = '123'

usrlist = {'admin':'1234'}

class MyMainForm(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.loginfunction) # 登陆按钮
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password) # 密码不显示
        self.pushButton_2.clicked.connect(self.gotosignup) #跳转到注册
        #self.pushButton_3.clicked.connect(self.close) #退出软件

    

    def loginfunction(self):
        #QMessageBox.information(self, "信息提示框", "OK,内置信号与自定义槽函数！")
        username_1=self.lineEdit.text()
        password_1=self.lineEdit_2.text()
        try:
            if usrlist[username_1] == password_1 :
                QMessageBox.information(self, "信息提示框", "登录成功！")


                mainwin=MyMainForm2()
                widget.addWidget(mainwin)

                widget.setFixedWidth(800)
                widget.setFixedHeight(620)

                # widget1 = QtWidgets.QStackedWidget()
                # widget1.addWidget(mainwin)
                # widget1.setFixedWidth(800)
                # widget1.setFixedHeight(620)

                widget.setCurrentIndex(widget.currentIndex()+1)

            else:
                QMessageBox.information(self, "信息提示框", "用户名或密码错误，请重新输入！")
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')
        
        except KeyError:
            QMessageBox.information(self, "信息提示框", "没有该用户名，如果没有注册，请点击注册按钮！")
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')


        # self.TZ = 
        
        
        #print("Successfully logged in with email: ", email, "and password:", password)

# 跳转界面
    def gotosignup(self):
        createacc=MyMainForm_1()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class MyMainForm_1(QMainWindow, Ui_Dialog1):



    def __init__(self, parent=None):
        super(MyMainForm_1, self).__init__(parent)
        self.setupUi(self)
        self.pushButton__.clicked.connect(self.signupfunction)
        self.lineEdit__2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit__3.setEchoMode(QtWidgets.QLineEdit.Password)


    def signupfunction(self):
        
        global usrlist
        
        username = self.lineEdit__.text()
        password = self.lineEdit__2.text()
        if username == ''or password == '':
            QMessageBox.information(self, "信息提示框", "用户名或密码不能为空，请重新输入！")
        else:
            if self.lineEdit__2.text() == self.lineEdit__3.text():
                username = self.lineEdit__.text()
                password = self.lineEdit__2.text()

                usrlist[username] = password

                #print("Successfully created acc with email: ", email, "and password: ", password)
                QMessageBox.information(self, "信息提示框", "注册成功！")
                login=MyMainForm()
                widget.addWidget(login)
                widget.setCurrentIndex(widget.currentIndex()+1)

            else:
                QMessageBox.information(self, "信息提示框", "密码不一致，请重新输入！")
                self.lineEdit__2.setText('')
                self.lineEdit__3.setText('')

        # password=self.lineEdit__2.text()
        # password=self.lineEdit__3.text()



# class MyMainForm(QMainWindow, Ui_Dialog):
#     def __init__(self, parent=None):
#         super(MyMainForm, self).__init__(parent)
#         self.setupUi(self)

# class MyMainForm_2(QMainWindow, Ui_MainWindow):
#     def __init__(self, parent=None):
#         super(MyMainForm_2, self).__init__(parent)
#         self.setupUi(self)


class MyMainForm2(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm2, self).__init__(parent)
        self.setupUi(self)

        self.pushButton___.clicked.connect(self.Classification)
        self.pushButton___1.clicked.connect(self.CBGI)
        self.actionOpen.triggered.connect(self.openimage)
        self.action.triggered.connect(self.closeimage)
        #self.action_2.triggered.connect(self.close)
        #self.pushButton___2.clicked.connect(self.closef)
        self.actionRed.triggered.connect(self.BGImage)
        self.actionGreen.triggered.connect(self.BGG)
        self.actionGray.triggered.connect(self.BGG1)
        self.actionBlack.triggered.connect(self.BGB)
        self.action_8.triggered.connect(self.BGI)
        self.action_6.triggered.connect(self.SCLink)
        #self.action_5.triggered.connect(self.PDFView)
        self.actionWhite.triggered.connect(self.BGW)

        self.action_4.triggered.connect(self.Aboutapp)
        self.action_5.triggered.connect(self.Help)
        self.action_7.triggered.connect(self.report)

        self.action_3.triggered.connect(self.information)
        self.pushButton___2.clicked.connect(self.backmain)

        self.actionRed_2.triggered.connect(self.BGRS)
        self.actionGreen_2.triggered.connect(self.BGGS)
        self.actionGray_2.triggered.connect(self.BGGS1)
        self.actionBlack_2.triggered.connect(self.BGBS)
        self.actionWhite_2.triggered.connect(self.BGWS)


    def openimage(self):
        QMessageBox.information(self, "信息提示框", "请不要用其它类型的图片测试！！！")
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "/home/jjyao/下载/archive", "All Files(*);;*.jpg;;*.png")

        jpg = QtGui.QPixmap(imgName).scaled(self.label___.width(), self.label___.height())
        self.label___.setPixmap(jpg)

    def CBGI(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "/home/jjyao/下载/archive", "All Files(*);;*.jpg;;*.png")

        jpg = QtGui.QPixmap(imgName).scaled(self.label___.width(), self.label___.height())
        self.label___.setPixmap(jpg)

    def closeimage(self):
        self.label___.setPixmap(QtGui.QPixmap(""))
        self.lineEdit___.setText('')


    def BGImage(self):
        self.label___4.setStyleSheet('background:rgb(239, 41, 41);')
    def BGG(self):
        self.label___4.setStyleSheet('background:rgb(138, 226, 52);')
    def BGG1(self):
        self.label___4.setStyleSheet('background:rgb(186, 189, 182);')
    def BGB(self):
        self.label___4.setStyleSheet('background:rgb(54, 54, 54);')
    def BGW(self):
        self.label___4.setStyleSheet("background:rgb(255, 255, 255);")
    def BGI(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "/home/jjyao/python_files/gui/maincode/", "All Files(*);;*.jpg;;*.png")
        jpg = QtGui.QPixmap(imgName).scaled(self.label___4.width(), self.label___4.height())
        self.label___4.setPixmap(jpg)
        # self.listView___.setStyleSheet('background-image: url("/home/jjyao/python_files/gui/maincode/images.jpeg")')


    def BGRS(self):
        self.label___.setStyleSheet('background:rgb(239, 41, 41);')
    def BGGS(self):
        self.label___.setStyleSheet('background:rgb(138, 226, 52);')
    def BGGS1(self):
        self.label___.setStyleSheet('background:rgb(186, 189, 182);')
    def BGBS(self):
        self.label___.setStyleSheet('background:rgb(54, 54, 54);')
    def BGWS(self):
        self.label___.setStyleSheet("background:rgb(255, 255, 255);")
    


    def Help(self):
        webbrowser.open('/home/jjyao/python_files/gui/maincode/t1.pdf')


    def backmain(self):
        number = QMessageBox.question(self,"提问对话框", "你要返回主界面吗？", QMessageBox.Yes | QMessageBox.No)
        if number != 65536:
            login=MyMainForm()
            widget.addWidget(login)

            # widget.addWidget(mainwin)
            widget.setFixedWidth(480)
            widget.setFixedHeight(620)

            widget.setCurrentIndex(widget.currentIndex()+1)

        else:
            pass


    def information(self):
        ul = '用户名列表：'
        for ul_1 in usrlist.keys():
            ul = ul+' \n'+ul_1 
        QMessageBox.information(self, "用户名列表", ul)

    # def closef(self):
    #     number = QMessageBox.question(self,"提问对话框", "你要退出登录吗？", QMessageBox.Yes | QMessageBox.No)
    #     if number != 65536:
    #         login=MyMainForm()
    #         widget.addWidget(login)
    #         widget.setCurrentIndex(widget.currentIndex()+1)

    
    def Aboutapp(self):
        QMessageBox.information(self, "信息提示框", "猫狗识别小软件，作者：jjyao \n 版本：1.0.0")
    def report(self):
        number = 1
        while number != 65536 :
            number = QMessageBox.question(self,"提问对话框", "你要report作者吗？", QMessageBox.Yes | QMessageBox.No)

        QMessageBox.information(self, "信息提示框", "举报失败！")
    def SCLink(self):
        QDesktopServices.openUrl(QUrl("https://github.com/jjyao-1/-pytorch-Resnet50-pyqt5-GUI-"))

    def Classification(self):
        img_Qt = self.label___.pixmap()
        img = ImageQt.fromqimage(img_Qt)

        data_transform = transforms.Compose(
            [transforms.Resize([224,224]),transforms.ToTensor(),transforms.Normalize(mean=[0.5,0.5,0.5],std=[0.5,0.5,0.5])]
        )

        img_ = data_transform(img).unsqueeze(0) #拓展维度

        cvd = ['cat','dog']

        model = models.resnet50(pretrained= True)
        model.fc = torch.nn.Linear(2048,2)

        model.load_state_dict(torch.load('/home/jjyao/python_files/gui/test/save.pt',map_location=torch.device('cpu')))
        # model.load_state_dict(torch.load(PATH))
        model.eval()

        X = img_
        outputs = model(X)

        _, pred = torch.max(outputs,1)

        Result = cvd[pred]
        self.lineEdit___.setText(Result)











if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #Form = QtWidgets.QWidget()
    #ui = Ui_Form()
    #ui.setupUi(Form)
    #Form.show()
    #初始化
    myWin = MyMainForm()
    myWin1 = MyMainForm2()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(myWin)
    widget.setFixedWidth(480)
    widget.setFixedHeight(620)
    widget.show()
    widget1 = QtWidgets.QStackedWidget()
    widget1.addWidget(myWin1)
    widget1.setFixedWidth(800)
    widget1.setFixedHeight(620)
    
    
    #将窗口控件显示在屏幕上
    #myWin.show()
    sys.exit(app.exec_())