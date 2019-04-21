import cv2
import time
import os
import numpy as np

import _2_4_faceDetM

def moveDet(frame, imgts, recordFlag):
    #getStructuringElement是获取常用的结构元素的形状，MORPH_ELLIPSE是椭圆（包括圆形），后面定义的是大小
    es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,4))
    kernel = np.ones((5,5),np.uint8)
    # 总是取第一帧做为背景（不用考虑环境影响）
    background = imgts[1]
    cutpoints = 0
    if background is None:#初始化背景，后面的图像均以此为背景,即第一张图
        imgts[0] = frame
        background =  cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)###灰度化图像
        background =  cv2.GaussianBlur(background,(21,21),0)###进行模糊处理
        imgts[1] = background
        # continue# 跳出这个循环
    else:
        gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.GaussianBlur(gray_frame,(21,21),0)
        #打开系统默认的摄像头获得的视频图像，并将第一帧设置为整个输入的背景
        #对于每个从该点以后读取的帧都会计算其与背景之间的差异
        diff = cv2.absdiff(background, gray_frame) #计算背景帧与当前帧的差值
        diff = cv2.threshold(diff,60,255,cv2.THRESH_BINARY)[1]#60为阈值，255为超过阈值被赋予的值
        diff = cv2.dilate(diff,es,iterations = 2)#进行图片膨胀，iterations为膨胀次数为2，
        #findContours函数计算一幅图像中目标的轮廓，diff.copy()为输入的二值单通道图像
        # 轮廓CV_RETR_EXTERNAL表示只检测外轮廓
        image,cnts,hierarchy = cv2.findContours(diff.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for c in cnts:
            if cv2.contourArea(c) < 5000:
                continue
            #c是一个二值图，boundingRect是矩形边框函数，用一个最小的矩形，把找到的形状包起来；
            #x,y是矩形左上点的坐标；w,h是矩阵的宽和高
            (x,y,w,h) = cv2.boundingRect(c)
            #rectangle画出矩形，frame是原图，(x,y)是矩阵的左上点坐标，(x+w,y+h)是矩阵右下点坐标
            #(0,255,0)是画线对应的rgb颜色，2是画线的线宽
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame, "Detect Move at time: {}".format(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))) ), (10, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            recordFlag[0] = True
            # print("出现目标物，请求核实")
            #人脸识别
            frame = _2_4_faceDetM.faceDet(frame, c, recordFlag)
            break
        imgts[0] = frame
