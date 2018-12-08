# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import getface
import update
import recognize

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.NameText = QtWidgets.QTextEdit(self.centralwidget)
        self.NameText.setGeometry(QtCore.QRect(590, 80, 161, 31))
        self.NameText.setObjectName("NameText")
        self.IDText = QtWidgets.QTextEdit(self.centralwidget)
        self.IDText.setGeometry(QtCore.QRect(590, 130, 161, 31))
        self.IDText.setObjectName("IDText")
        self.NameLabel = QtWidgets.QLabel(self.centralwidget)
        self.NameLabel.setGeometry(QtCore.QRect(530, 80, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        self.NameLabel.setFont(font)
        self.NameLabel.setObjectName("NameLabel")
        self.IDLabel = QtWidgets.QLabel(self.centralwidget)
        self.IDLabel.setGeometry(QtCore.QRect(540, 140, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        self.IDLabel.setFont(font)
        self.IDLabel.setObjectName("IDLabel")
        self.getfaceButton = QtWidgets.QPushButton(self.centralwidget)
        self.getfaceButton.setGeometry(QtCore.QRect(580, 210, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.getfaceButton.setFont(font)
        self.getfaceButton.setObjectName("getfaceButton")
        self.updateButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateButton.setGeometry(QtCore.QRect(580, 280, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.updateButton.setFont(font)
        self.updateButton.setObjectName("updateButton")
        self.recognizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.recognizeButton.setGeometry(QtCore.QRect(580, 350, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.recognizeButton.setFont(font)
        self.recognizeButton.setObjectName("recognizeButton")
        self.AttendText = QtWidgets.QTextEdit(self.centralwidget)
        self.AttendText.setGeometry(QtCore.QRect(40, 90, 151, 311))
        self.AttendText.setObjectName("AttendText")
        self.AttendLabel = QtWidgets.QLabel(self.centralwidget)
        self.AttendLabel.setGeometry(QtCore.QRect(80, 70, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        self.AttendLabel.setFont(font)
        self.AttendLabel.setObjectName("AttendLabel")
        self.AbsentText = QtWidgets.QTextEdit(self.centralwidget)
        self.AbsentText.setGeometry(QtCore.QRect(280, 90, 151, 311))
        self.AbsentText.setObjectName("AbsentText")
        self.AbsentLabel = QtWidgets.QLabel(self.centralwidget)
        self.AbsentLabel.setGeometry(QtCore.QRect(320, 70, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        self.AbsentLabel.setFont(font)
        self.AbsentLabel.setObjectName("AbsentLabel")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(290, 460, 431, 91))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.NameLabel.setText(_translate("MainWindow", "Name"))
        self.IDLabel.setText(_translate("MainWindow", "ID"))
        self.getfaceButton.setText(_translate("MainWindow", "人脸录入"))
        self.updateButton.setText(_translate("MainWindow", "更新人脸"))
        self.recognizeButton.setText(_translate("MainWindow", "开始检测"))
        self.AttendLabel.setText(_translate("MainWindow", "Attend"))
        self.AbsentLabel.setText(_translate("MainWindow", "Absent"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Tips:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">录入人脸或更新人脸信息时请先输入姓名和学号再按相应按键</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">摄像头调用后请按&quot;s&quot;存储人脸信息</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">信息存储完毕后请按&quot;q&quot;关闭摄像头</p></body></html>"))
  
    #以下三个函数为槽函数
    def get_face(self):
        NAME = self.NameText.toPlainText()
        SNUM = self.IDText.toPlainText()
        ID = SNUM+NAME
        getface.get(ID)
    
    def update_face(self):
        NAME = self.NameText.toPlainText()
        SNUM = self.IDText.toPlainText()
        ID = SNUM+NAME
        update.get1(ID)
        
    def recognise(self):
        absent = []
        attend = []
        absent_string = ' '
        attend_string = ' '
        absent,attend = recognize.reco()
        for absent_student in absent:
            absent_string = absent_string+absent_student+'\n'
        for attend_student in attend:
            attend_string = attend_string+attend_student+'\n'
        self.AbsentText.setText(absent_string)
        self.AttendText.setText(attend_string)