# Exercise
基于人脸识别的自动点名程序(带GUI操作界面)  

环境与系统包   
Win10+Anaconda3+python3.6  
import face_recognition  
import cv2  
import PyQt5

设计思路  

1.存储所有同学的人脸信息（getface.py）  
调用opencv摄像头存储图像，分析该图像人脸数据并将信息保存至本地。  

2.实时检测，分别输出到场同学和翘课同学的姓名和学号(recognize.py)  
调用opencv摄像头存储图像，分析图像中所有人脸的数据。将getface.py存储在本地的人脸数据与刚刚得到的数据进行对比。  

3.若图像存储时没有拍好(如闭眼等）可能会降低识别准确度，所以需要更新人脸信息的功能(update.py)  
基本重复getface.py的操作，将原文件覆盖。  

4.为方便操作利用pyqt5设计图形界面(face_ui.py)  
利用designer构建出界面样式，再添加事件监听  

5.将窗口初始化并显示(ui_start.py)  
