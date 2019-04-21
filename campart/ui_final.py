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
    root = tkinter.Tk()
    root.title('CamProject')
    frame = Frame(root)
    frame.pack()
    usrla = Label(frame, text = '账号：').grid(row = 0, column = 0, padx = 20, pady = 10)
    pasla = Label(frame, text = '账号：').grid(row = 1, column = 0, padx = 20, pady = 10)
    usret = Entry(frame)
    usret.grid(row = 0, column = 1, padx = 20, pady = 10)
    paset = Entry(frame)
    paset.grid(row = 1, column = 1, padx = 20, pady = 10)
    msgla = Label(frame, text = '请输入账号密码')
    msgla.grid(row = 2, column = 1, sticky = W, padx = 20, pady = 10)
    def validUser():
        userc = usret.get()
        passc = paset.get()
        print (userc + '   ' + passc)
        userflag = usercheck.user_check(userc, passc)
        if (userflag[0] == 0):
            msgla.configure(text = "用户名密码错误！")
        else:
            wxid = userflag[1]
            msgla.configure(text = "登录成功！")
            print ('\n' + wxid)
    def registerUser():
        print ('s')
    validbt = Button(frame, text = '登录', command = validUser).grid(row = 2,\
        column = 1, sticky = E, padx = 20, pady = 10)
    registerbt = Button(frame, text = '注册', command = registerUser).grid(row = 2,\
        column = 0, sticky = W, padx = 20, pady = 10)
    # atk刷新时间显示
    atklabel = Label(frame, text = 'ATK刷新时间:00:00')
    atklabel.grid(row = 3, column = 1, sticky = E, padx = 10, pady = 5)
    def atktimeupdate():
        showtime = 'ATK刷新时间:' + str(int(atktime[0]) // 60) + ':'
        showtime += str(int(atktime[0]) - 60 * (int(atktime[0]) // 60))
        atklabel.configure(text = showtime)
        atklabel.after(1000,atktimeupdate)
    atklabel.after(0,atktimeupdate)


    root.mainloop()

#程序开始--多线程
#处理atk线程
_thread.start_new_thread(wxgetatk.get_atk,(atktime,))
#开始主体模块线程
_thread.start_new_thread(f_start,(atktime,))
while 1:
    pass
