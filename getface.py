import cv2
import face_recognition
import os
import pickle 

    
def get(ID): 
  #ID = input("ID+NAME:")  
  #调用摄像头，按's'截图保存，按'q'关闭摄像头
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

# 将jpg文件加载到numpy 数组中
  image = face_recognition.load_image_file("C:/Users/zhanghang/Desktop/face/"+ID+".jpg")
  image_new = image[:, :, ::-1]

  face_encoding = face_recognition.face_encodings(image_new)[0]

  #将ID和人脸信息存成字典保存在本地
  size = os.path.getsize('C:/Users/zhanghang/Desktop/All_facecode.dat')
  if size == 0:
    dict={ID:face_encoding}
  else:
    f = open('C:/Users/zhanghang/Desktop/All_facecode.dat','rb')
    dict = pickle.load(f)
    f.close()
    dict[ID]=face_encoding

  f = open('C:/Users/zhanghang/Desktop/All_facecode.dat','wb')
  pickle.dump(dict,f)
  f.close()  