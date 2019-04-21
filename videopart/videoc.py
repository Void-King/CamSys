# coding:utf-8
import cv2
import sys
cap = cv2.VideoCapture(0)
sz = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# 第三个参数则是镜头快慢的，10为正常，小于10为慢镜头
out = cv2.VideoWriter('./output2.mp4', fourcc,20,sz,True)
for i in range(0,60):
    ret,frame = cap.read()
    if ret == True:
        # cv2.imwrite('./output2.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 60])
        frame = cv2.flip(frame, 1)
        out.write(frame)
        # cv2.imshow("frame", frame)
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()