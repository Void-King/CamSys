import cv2
import time
import os

def faceDet(img, recordFlag):
    try:
        facexml = r"./pic/haarcascade_frontalface_default.xml"
        face_cascade = cv2.CascadeClassifier(facexml)
        grayOfFacedet = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(grayOfFacedet, 1.3, 5)
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + w), (0, 255, 0), 2)
            cv2.putText(img, "Detect Faces", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            recordFlag[1] = True
            # cv2.imwrite(pathAndName, imageOfFacedet)
            # print (pathAndName)
            # # token = wxgetatk.use_atk()
            # # wxsentpic.set2user(wxid, token, pathAndName)
            # cv2.imshow("faceDetected", imageOfFacedet)
        return img
    except:
        # print ('Program Wrong 5')
        log = open(r'./wronglog.ini', 'a')
        log.write('Program wrong 5\n')
        log.close()
        return img