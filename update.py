# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 21:20:07 2018

@author: zhanghang
"""

import cv2
import face_recognition
import pickle 
 
def get1(ID):
#ID = input("ID+NAME:")

    cap=cv2.VideoCapture(0)

    while(1):
        ret,frame = cap.read()
        k=cv2.waitKey(1)
        if k==ord('q'):
            break
        elif k==ord('s'):
            cv2.imwrite('C:/Users/zhanghang/Desktop/face/'+ID+'.jpg',frame) 
        
        cv2.imshow("capture",frame)
            
    cap.release()
    cv2.destroyAllWindows()

    image = face_recognition.load_image_file("C:/Users/zhanghang/Desktop/face/"+ID+".jpg")
    image_new = image[:, :, ::-1]

    face_encoding = face_recognition.face_encodings(image_new)[0]

    f = open('C:/Users/zhanghang/Desktop/All_facecode.dat','rb')
    dict = pickle.load(f)
    f.close()
    dict[ID]=face_encoding

    f = open('C:/Users/zhanghang/Desktop/All_facecode.dat','wb')
    pickle.dump(dict,f)
    f.close()