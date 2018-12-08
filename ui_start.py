# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 16:28:40 2018

@author: zhanghang
"""

import sys
from PyQt5 import QtWidgets
import face_ui  
 
Ui_MainWindow = face_ui.Ui_MainWindow

class CoperQt(QtWidgets.QMainWindow,Ui_MainWindow):#创建一个Qt对象
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)  # 创建主界面对象
        Ui_MainWindow.__init__(self)#主界面对象初始化
        self.setupUi(self)  #配置主界面对象
        self.getfaceButton.clicked.connect(lambda:face_ui.Ui_MainWindow.get_face(self))
        self.updateButton.clicked.connect(lambda:face_ui.Ui_MainWindow.update_face(self))
        self.recognizeButton.clicked.connect(lambda:face_ui.Ui_MainWindow.recognise(self))

if __name__ == "__main__":
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    window = CoperQt()#创建QT对象
    window.show()#QT对象显示
    sys.exit(app.exec_())
