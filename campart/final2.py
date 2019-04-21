import cam
import delfile
import mysql
import wxgetatk
import wxsent2user
import _thread
import time
import usercheck
import os
import wxsentpic
import requests
import tkinter
from tkinter import *
#截图保存地址
save_path = r'./cam1/pic/'

#atk更新时间倒数
atktime = [3600,]

def f_start(atktime):
    # while (True):
    #     print (atktime[0])
    #     time.sleep(1)
    userc = input ('user:')
    passc = input ('pass:')
    #用户检测模块 根据用户名密码得到用户微信号openid
    userflag = usercheck.user_check(userc, passc)
    while(userflag[0] == 0):
        print ("用户名密码错误！")
        userc = input ('user:')
        passc = input ('pass:')
        userflag = usercheck.user_check(userc, passc)
    wxid = userflag[1]
    print ('\n' + wxid)
    
    # #获取atk
    # token = wxgetatk.use_atk()
    # print('\n' + token)
    # #test
    # msg = input("发送内容:")
    # wxsent2user.set2user(wxid, token, msg)

    cam.cam_start(save_path, wxid)

    #是否删除使用过的图片
    i = int(input ("是否删除保存的图片 是（1） 否（0）:"))
    if i == 1:
        delfile.del_file(save_path)
    # print ("请手动关闭程序")
    os._exit(0)

#程序开始--多线程
#处理atk线程
_thread.start_new_thread(wxgetatk.get_atk,(atktime,))
#开始主体模块线程
_thread.start_new_thread(f_start,(atktime,))
while 1:
    pass
