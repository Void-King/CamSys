import tkinter as tk
from tkinter import *
import time
import os
import _1_4_vaildRegisterM

def addUserUI():
    root = tk.Tk()
    root.iconbitmap('./pic/Cam.ico')
    root.title('Register')
    root.resizable(0, 0)
    frame = tk.Frame(root)
    frame.pack()

    usrla = Label(frame, text = '账号：').grid(row = 0, column = 0, padx = 20, pady = 10)
    pasla = Label(frame, text = '密码：').grid(row = 1, column = 0, padx = 20, pady = 10)
    wxila = Label(frame, text = '微信ID：').grid(row = 2, column = 0, padx = 20, pady = 10)
    usret = Entry(frame)
    usret.grid(row = 0, column = 1, padx = 20, pady = 10)
    paset = Entry(frame)
    paset.grid(row = 1, column = 1, padx = 20, pady = 10)
    wxila = Entry(frame)
    wxila.grid(row = 2, column = 1, padx = 20, pady = 10)
    wxila.insert(0,'请联系管理员获得')
    msgla = Label(frame, text = '请输入账号信息')
    msgla.grid(row = 3, column = 1, sticky = W, padx = 20, pady = 10)
    # 登录按键事件
    def confirmBC():
        userc = usret.get()
        passc = paset.get()
        wxidc = wxila.get()
        userFlag = _1_4_vaildRegisterM.vaildRegisterUser(userc, passc, wxidc)
        if userFlag == 0:
            root1 = tk.Tk()
            root1.title('!')
            label1 = tk.Label(root1, text = '注册成功！').pack(padx = 60, pady = 10)
            def confirmBC1():
                root1.destroy()
                root.destroy()
            confirmbt1 = Button(root1, text = '确认', command = confirmBC1\
                ).pack(padx = 60, pady = 10)
            root1.mainloop()
        elif userFlag == 1:
            msgla.configure(text = '用户名已存在')
        elif userFlag == 2:
            msgla.configure(text = '微信ID错误')
        elif userFlag == 3:
            msgla.configure(text = '不能为空')
        else:
            # print ('Program wrong 2')
            log = open(r'./wronglog.ini','a')
            log.write('Program wrong 2\n')
            log.close()
    
    confirmbt = Button(frame, text = '确认', command = confirmBC).grid(row = 3,\
        column = 1, sticky = E, padx = 20, pady = 10)
    root.mainloop()