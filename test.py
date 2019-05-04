# # import _1_5_sentSQLM
# # import _2_5_wxSentM
# # import time
# # while True:
# #     atk = '20_a17yWRROOK1wZkfIN-cqKT1libEpIY7hm8VW72yf5bQmPgMM_PFNkQiXdndQefkQfdQtBlWqGzkwzb2OdDDLMOzT7TEyRJ-m9VWkHC7yJgr2J3sxDZM3hAl-YVhiy8Ct0RvK-M1WRxXpTx0KVERcABAOXK'
# #     wxid = 'o__Cr1Y4gVbFpJv18yUdHN7cr4RI'
# #     sql = "SELECT * FROM `user_list` WHERE `wxid`=\'" + wxid + "\'"
# #     data = _1_5_sentSQLM.sql_sent(sql)
# #     times = data[0][3]
# #     request = data[0][4]
# #     print (data)
# #     print (str(times))
    
# #     print (request)
# #     if request == 1:
# #         _2_5_wxSentM.setm2user(wxid, atk, 'tpfs')
# #         times += 1
# #         sql = '''UPDATE `user_list`
# #             SET `times` = \'''' + str(times) + '''\',`request` = '0'
# #             WHERE `wxid` = \'''' + wxid + '''\';
# #             '''
# #         _1_5_sentSQLM.sql_sent(sql)
# #         print ('ok')
# #     time.sleep(2)
# # a = 'zt80'
# # print (str(a)[0:2])
# # print (len(a))
# # if str(a)[0:2] == 'zt':
# #     c = 0
# #     try:
# #         c = int(str(a)[2:])
# #         if 0 < c <= 90:
# #             print (int(str(a)[2:]))
# #             print ('系统已暂停' +str(a)[2:] + '分钟')
# #         else:
# #             print('sadf')
# #     except:
# # #         pass
# # import cv2
# # camera = cv2.VideoCapture(1)
# # while True:
# #     suc, img = camera.read()
# #     cv2.imshow('title',img)
# #     cv2.waitKey(200)
# # camera.release()
# # cv2.destroyAllWindows()
# log = open(r'./wronglog.ini','a')
# print (type(log))
# log.close()

# def moveDet(img, imgts, recordFlag):
# # 取图像信息地址背景图
# background = imgts[1]
# cutpoints = 0
# if background is None:#若背景图不存在或已复位，初始化背景
#     imgts[0] = img
#     background =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     # 灰度图转换
#     background =  cv2.GaussianBlur(background,(21,21),0)
#     # 进行模糊处理
#     imgts[1] = background
# else:
#     # 灰度图
#     grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     grayimg = cv2.GaussianBlur(grayimg,(21,21),0)

#     calcudf = cv2.absdiff(background, grayimg) #计算差值
#     calcudf = cv2.threshold(calcudf,60,255,
#                             cv2.THRESH_BINARY)[1]
#     # 60为阈值，255为最大值
#     calcudf = cv2.dilate(calcudf,es,iterations = 2)
#     # 进行2次图片膨胀，
#     # findContours函数计算目标轮廓
#     # CV_RETR_EXTERNAL 检测外轮廓
#     # cs为检测出的轮廓的二值图列表
#     image,cs,hierarchy = cv2.findContours(calcudf.copy(),
#                 cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#     for c in cs:
#         # 跳过过小的或未连同的像素点
#         if cv2.contourArea(c) < 5000:
#             continue
#         # boundingRect是矩形边框函数，
#         # 用矩形框柱移动物体；
#         # x,y是矩形左上点的坐标；w,h是矩阵的宽和高
#         (x,y,w,h) = cv2.boundingRect(c)
#         # rectangle花矩形函数,img是原图，
#         # (x,y)是矩阵的左上点坐标，
#         # (x+w,y+h)是矩阵右下点坐标
#         # (0,255,0)是线对应颜色，2是线宽
#         cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)
#         cv2.putText(img, "Detect Move at time: {}\
#             ".format(str(time.strftime('%Y-%m-%d %H:%M:%S',
#             time.localtime(time.time()))) ), (10, 20),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.6,
#                                 (0, 0, 255), 2)
#         # 移动检测报警
#         recordFlag[0] = True
#         #人脸识别
#         img = _2_4_faceDetM.faceDet(img, recordFlag)
#         break
#     imgts[0] = img


# def faceDet(img, recordFlag):
#     # 载入人脸检测训练集
#     facexml = r"./pic/haarcascade_frontalface_default.xml"
#     # 得到人脸检测级联表
#     face_cascade = cv2.CascadeClassifier(facexml)
#     # 转灰度图
#     grayOfFacedet = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # 目标检测函数 检测人脸
#     faces = face_cascade.detectMultiScale(grayOfFacedet,
#                                           1.3, 5)
#     # 处理人脸
#     if len(faces) > 0:
#         for (x, y, w, h) in faces:
#             # 用矩形把人脸框住
#             cv2.rectangle(img, (x, y), (x + w, y + w),
#                           (0, 255, 0), 2)
#         cv2.putText(img, "Detect Faces", (10, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7,
#                     (0, 0, 255), 2)
#         # 人脸检测报警
#         recordFlag[1] = True
#     return img
strpn = '' + time.strftime('%Y-%m-%d %H.%M.%S',time.localtime(time.time()))
strpnfd = re.sub('\.+', ':', strpn)
sqle = r"INSERT INTO alarm_inf VALUES ('" + username + r"', '\
        " + strpnfd + r"', '用户登录')"
_1_5_sentSQLM.sql_sent(sqle)