# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:40:42 2018

@author: zhanghang
"""

import face_recognition
import cv2
import pickle
import shutil
import os

def reco():   
  f = open('C:/Users/zhanghang/Desktop/All_facecode.dat','rb')
  dict = pickle.load(f)
  f.close()

  All_id = list(dict.keys())
  All_facecode = list(dict.values())

#识别开始前清空文件内容
  shutil.rmtree('C:/Users/zhanghang/Desktop/face_part')
  os.mkdir('C:/Users/zhanghang/Desktop/face_part')
  shutil.rmtree('C:/Users/zhanghang/Desktop/face_test')
  os.mkdir('C:/Users/zhanghang/Desktop/face_test')

  attend=[]
  absent=[]

  cap=cv2.VideoCapture(0)

  while(1):
    ret ,frame = cap.read()
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
    elif k==ord('s'):
        cv2.imwrite('C:/Users/zhanghang/Desktop/face_test/test.jpg',frame)
        
    
    cv2.imshow("capture", frame)
  cap.release()
  cv2.destroyAllWindows()

# 将jpg文件加载到numpy 数组中
  image = face_recognition.load_image_file("C:/Users/zhanghang/Desktop/face_test/test.jpg")
  image_new = image[:, :, ::-1]

  face_locations = face_recognition.face_locations(image_new)
  face_encodings = face_recognition.face_encodings(image_new,face_locations)

  j=0
  for face_location in face_locations:
        jj=str(j)
        # 打印每张脸的位置信息
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right)) 
        # 指定人脸的位置信息，然后保存人脸图片
        face_image = image_new[top:bottom, left:right]
        cv2.imwrite('C:/Users/zhanghang/Desktop/face_part/'+jj+'.jpg',face_image) 
        j=j+1
  
#比较人脸数据      
  i=0
  for face_encoding in All_facecode:
      matches = face_recognition.compare_faces(face_encoding, face_encodings,0.4)
      if True in matches:
        ID = All_id[i]
        attend.append(ID)
      else:
        ID = All_id[i]
        absent.append(ID)
      i=i+1
  
  return absent,attend