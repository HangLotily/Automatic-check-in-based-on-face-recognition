# Exercise
基于人脸识别的自动点名程序(带GUI操作界面)

环境与系统包
-----
  Win10+Anaconda3+python3.6
  import face_recognition
  import cv2
  import PyQt5

  
设计思路
-----
1.存储所有同学的人脸信息（getface.py）
  调用opencv摄像头存储图像，分析该图像人脸数据并将信息保存至本地。

2.实时检测，分别输出到场同学和翘课同学的姓名和学号(recognize.py)
  调用opencv摄像头存储图像，分析图像中所有人脸的数据。将getface.py存储在本地的人脸数据与刚刚得到的数据进行对比。

3.若图像存储时没有拍好(如闭眼等）可能会降低识别准确度，所以需要更新人脸信息的功能(update.py)
  基本重复getface.py的操作，将原文件覆盖。

4.为方便操作利用pyqt5设计图形界面(face_ui.py)
  利用designer构建出界面样式，再添加事件监听

5.将窗口初始化并显示(ui_start.py)


具体实现
-----
1.getface.py  
  调用摄像头，实现按'q'退出，按‘s’通过cv2.imwrite()函数将这一帧的画面存储在本地，命名为ID.jpg  
  通过face_recognition.load_image_file()函数将保存好的图像加载进来  
  通过face_recognition.face_encodings()函数提取人脸信息，返回的是128维向量  
  △难点：将ID和人脸信息对应并保存至本地  
    采用的是字典并以二进制形式保存的方式。通过dict={ID:face_encoding}记录第一位同学的信息，利用pickle.dump(dict,f)将字典以二进制保存至本地。当记录下一位同学的信息时，先将之前的字典信息加载进来，生成新的字典后在保存  
  至此，完成每位同学人脸信息的存储  

2.recognize.py  
  通过dict = pickle.load(f)加载本地字典数据  
  调用摄像头，实现按'q'退出，按‘s’通过cv2.imwrite()函数将这一帧的画面存储在本地，命名为test.jpg  
  通过face_recognition.load_image_file()函数将保存好的图像加载进来  
  通过face_recognition.face_encodings()函数提取每一张人脸的信息，命名为face_encodings  
  利用循环与face_recognition.compare_faces(face_encoding, face_encodings,0.4)函数，将字典中每一张人脸信息的128维向量分别与face_encodings中人脸信息的向量进行比较，阈值<0.4代表人脸匹配，将ID加入列表Attend[]，若均未能匹配代表该同学未来上课，将ID加入列表Absent[]   

3.update.py  
  基本重复getface.py的操作,将旧的图片与人脸信息覆盖  

4.face_ui.py  
  先通过designer拖出界面样式保存为face_ui.ui，再通过命令pyuic.py "ui文件路径" -o "py文件路径" 生成face_ui.py文件  
  修改face_ui.py，添加了三个槽函数：  
  def get_face(self)：通过toPlainText()函数从图形界面中读取ID值并调用getface.py实现人脸信息存储  
  def update_face(self):通过toPlainText()函数从图形界面中读取ID值并调用update.py实现人脸信息更新  
  def recognise(self):调用recognize.py 实现人脸识别，并对结果进行字符串处理，通过setText()函数将结果输出至图形界面  

5.ui_start.py  
  对窗口进行初始化并实现窗口的显示  
  通过self.Button.clicked.connect()函数将槽函数与按钮连接  
  
程序运行
-----
  执行ui_start.py即可  
  
示例图片
-----
![示例](https://github.com/HangLotily/Exercise/blob/master/example/example.png)
