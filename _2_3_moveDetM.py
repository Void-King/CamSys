import cv2
import time
import os
import numpy as np

import _2_4_faceDetM

def moveDet(img, imgts, recordFlag):
    #getStructuringElement是获取常用的结构元素的形状，MORPH_ELLIPSE是椭圆，后面定义的是大小
    es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,4))
    kernel = np.ones((5,5),np.uint8)
    # 取图像信息地址背景图
    background = imgts[1]
    cutpoints = 0
    if background is None:#若背景图不存在或已复位，初始化背景
        imgts[0] = img
        background =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)# 灰度图转换
        background =  cv2.GaussianBlur(background,(21,21),0)# 进行模糊处理
        imgts[1] = background
    else:
        # 灰度图
        grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        grayimg = cv2.GaussianBlur(grayimg,(21,21),0)

        calcudf = cv2.absdiff(background, grayimg) #计算差值
        calcudf = cv2.threshold(calcudf,60,255,cv2.THRESH_BINARY)[1]#60为阈值，255为超过阈值被赋予的值
        calcudf = cv2.dilate(calcudf,es,iterations = 2)#进行图片膨胀，膨胀次数为2，
        # findContours函数计算目标轮廓
        # 轮廓CV_RETR_EXTERNAL表示只检测外轮廓 cs为检测出的轮廓的二值图列表
        image,cs,hierarchy = cv2.findContours(calcudf.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for c in cs:
            # 跳过过小的或未连同的像素点
            if cv2.contourArea(c) < 5000:
                continue
            # boundingRect是矩形边框函数，用矩形把找到的形状包起来；
            # x,y是矩形左上点的坐标；w,h是矩阵的宽和高
            (x,y,w,h) = cv2.boundingRect(c)
            # rectangle花矩形函数,img是原图，(x,y)是矩阵的左上点坐标，(x+w,y+h)是矩阵右下点坐标
            # (0,255,0)是线对应颜色，2是线宽
            cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img, "Detect Move at time: {}".format(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))) ), (10, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            recordFlag[0] = True
            #人脸识别
            img = _2_4_faceDetM.faceDet(img, recordFlag)
            break
        imgts[0] = img
