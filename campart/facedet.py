import cv2
import time
import os
import wxgetatk
import wxsentpic
def face_det(pathAndName, c, wxid):
    face_cascade = cv2.CascadeClassifier(r"./cam1/haarcascade_frontalface_default.xml")
    imageOfFacedet = cv2.imread(pathAndName)
    grayOfFacedet = cv2.cvtColor(imageOfFacedet,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayOfFacedet,1.3,5)
    if len(faces) > 0:
        print ("发现{0}个人脸!".format(len(faces)))
        (x, y, w, h) = cv2.boundingRect(c)
        for(x,y,w,h) in faces:
            cv2.rectangle(imageOfFacedet,(x,y),(x+w,y+w),(0,255,0),2)
        cv2.imwrite(pathAndName, imageOfFacedet)
        print (pathAndName)
        token = wxgetatk.use_atk()
        wxsentpic.set2user(wxid, token, pathAndName)
        cv2.imshow("faceDetected", imageOfFacedet)