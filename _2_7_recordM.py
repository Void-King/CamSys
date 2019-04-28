import time
import sys
import os
import cv2
import _2_5_wxSentM
import _1_5_sentSQLM
# import _2_2_atkM

def record(imgts, atktime, save_path, wxid, recordFlag, sz):
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')# 视频格式
    while True:
        time.sleep(0.7)# 循环间隔
        if atktime[0] == -1:#程序退出判断
            sys.exit(0)
        #获取用户已发送信息次数与用户申请信息
        sql = "SELECT * FROM `user_list` WHERE `wxid`=\'" + wxid + "\'"
        data = _1_5_sentSQLM.sql_sent(sql)
        times = data[0][3]
        request = data[0][4]
        # print (times)
        # print (request)
        #用户申请视频2优先判断，优先级1
        #用户申请图片1优先判断，优先级2
        #用户暂停/继续运行请求，优先级3
        #用户连接次数(20次限制)信息判断，优先级4
        #人脸报警发送信息判断，优先级5
        #移动物体报警发送信息判断，优先级6

        #用户申请视频优先判断，优先级1
        if request == 2:
            times += 1
            # print (times)
            strpn = '' + time.strftime('%Y.%m.%d.%H.%M.%S',time.localtime(time.time()))
            strpn = save_path + strpn + '.mp4'
            cv2.imwrite(strpn + '.jpg', imgts[0], [int(cv2.IMWRITE_JPEG_QUALITY), 60])
            out = cv2.VideoWriter(strpn,fourcc,120,sz[0],True)
            for i in range(0,720):
                frame = cv2.flip(imgts[0], 1)
                out.write(imgts[0])
            out.release()
            atk = atktime[1]
            _2_5_wxSentM.setv2user(wxid, atk, strpn + '.jpg', strpn)
            sql = '''UPDATE `user_list`
                SET `times` = '1',`request` = '0'
                WHERE `wxid` = \'''' + wxid + '''\';
                '''
            _1_5_sentSQLM.sql_sent(sql)
            log = open(r'./wronglog.ini','a')
            log.write('Get Video\n')
            log.close()
            time.sleep(0.3)
        #用户申请图片1优先判断，优先级2
        elif request == 1:
            times += 1
            # print (times)
            strpn = '' + time.strftime('%Y.%m.%d.%H.%M.%S',time.localtime(time.time()))
            strpn = save_path + strpn + ".jpg"
            cv2.imwrite(strpn, imgts[0])
            atk = atktime[1]
            _2_5_wxSentM.setp2user(wxid, atk, strpn)
            sql = '''UPDATE `user_list`
                SET `times` = '1',`request` = '0'
                WHERE `wxid` = \'''' + wxid + '''\';
                '''
            _1_5_sentSQLM.sql_sent(sql)
            log = open(r'./wronglog.ini','a')
            log.write('Get Picture\n')
            log.close()
            time.sleep(0.3)
        #用户暂停请求，优先级3
        elif str(request)[0:1] == '3':
            times += 1
            ptime = int(str(request)[1:])
            ptime *= 60
            # print (ptime)
            for i in range(0, ptime):
                if atktime[0] == -1:#程序退出判断
                    sys.exit(0)
                sql = "SELECT * FROM `user_list` WHERE `wxid`=\'" + wxid + "\'"
                data = _1_5_sentSQLM.sql_sent(sql)
                request = data[0][4]
                if request == 4:
                    break
                # print (i)
                time.sleep(0.9)
            sql = '''UPDATE `user_list`
                SET `times` = '1',`request` = '0'
                WHERE `wxid` = \'''' + wxid + '''\';
                '''
            recordFlag[0] = False
            recordFlag[1] = False
            _1_5_sentSQLM.sql_sent(sql)
            print ('start')
        elif request == 4:
            pass
        #用户次数信息判断，优先级4
        elif times == 19:
            times += 1
            # print (times)
            atk = atktime[1]
            content = '发送次数将到达限制，请回复任意词更新链接'.encode("utf-8").decode("latin1")
            _2_5_wxSentM.setm2user(wxid, atk, content)
            sql = '''UPDATE `user_list`
                SET `times` = \'''' + str(times) + '''\'
                WHERE `wxid` = \'''' + wxid + '''\';
                '''
            _1_5_sentSQLM.sql_sent(sql)
            time.sleep(0.3)

        elif times > 19:
            time.sleep(1)
            pass
        #人脸判断，优先级5
        elif recordFlag[1]:
            times += 1
            # print (times)
            strpn = '' + time.strftime('%Y.%m.%d.%H.%M.%S',time.localtime(time.time()))
            strpn = save_path + strpn + '.mp4'
            cv2.imwrite(strpn + '.jpg', imgts[0], [int(cv2.IMWRITE_JPEG_QUALITY), 60])
            out = cv2.VideoWriter(strpn,fourcc,120,sz[0],True)
            for i in range(0,720):
                frame = cv2.flip(imgts[0], 1)
                out.write(imgts[0])
            out.release()
            atk = atktime[1]
            _2_5_wxSentM.setv2user(wxid, atk, strpn + '.jpg', strpn)
            sql = '''UPDATE `user_list`
                SET `times` = \'''' + str(times) + '''\'
                WHERE `wxid` = \'''' + wxid + '''\';
                '''
            _1_5_sentSQLM.sql_sent(sql)
            recordFlag[1] = False
            recordFlag[0] = False
            time.sleep(0.3)
        #移动物体判断，优先级6
        elif recordFlag[0]:
            times += 1
            # print (times)
            time.sleep(0.7)# 等待物体主体进入画面
            strpn = '' + time.strftime('%Y.%m.%d.%H.%M.%S',time.localtime(time.time()))
            strpn = save_path + strpn + ".jpg"
            cv2.imwrite(strpn, imgts[0])
            atk = atktime[1]
            _2_5_wxSentM.setp2user(wxid, atk, strpn)
            sql = '''UPDATE `user_list`
                SET `times` = \'''' + str(times) + '''\'
                WHERE `wxid` = \'''' + wxid + '''\';
                '''
            _1_5_sentSQLM.sql_sent(sql)
            for i in range(0, 6):
                if recordFlag[1]:
                    break
                else:
                    time.sleep(0.5)
            recordFlag[0] = False
        #错误情况
        else:
            pass