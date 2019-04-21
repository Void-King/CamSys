import tkinter as tk
from tkinter import *
import os

import _1_2_vaildLoginM
import _1_3_addUserUIM
import _2_1_camUIM

save_path = './pic/movesave/'

def loginSubUI():
    root = tk.Tk()
    root.iconbitmap('./pic/Cam.ico')
    root.title('Login')
    root.resizable(0, 0)
    frame = tk.Frame(root)
    frame.pack()

    usrla = Label(frame, text = '账号：').grid(row = 0, column = 0, padx = 20, pady = 10)
    pasla = Label(frame, text = '密码：').grid(row = 1, column = 0, padx = 20, pady = 10)
    usret = Entry(frame)
    usret.grid(row = 0, column = 1, padx = 20, pady = 10)
    paset = Entry(frame)
    paset['show'] = '*'
    paset.grid(row = 1, column = 1, padx = 20, pady = 10)
    msgla = Label(frame, text = '请输入账号密码')
    msgla.grid(row = 2, column = 1, sticky = W, padx = 20, pady = 10)
    # 登录按键事件
    def loginBC():
        userc = usret.get()
        passc = paset.get()
        userFlag = _1_2_vaildLoginM.vaildLoginUser(userc, passc)
        if userFlag[0] == 0:
            msgla.configure(text = '登录成功')
            wxid = userFlag[1]
            # print (wxid)#得到wxid
            # 进入监控窗口
            root.destroy()
            _2_1_camUIM.camUI(save_path, wxid)
        elif userFlag[0] == 1:
            msgla.configure(text = '密码错误')
        elif userFlag[0] == 2:
            msgla.configure(text = '用户不存在')
        elif userFlag[0] == 3:
            msgla.configure(text = '不能为空')
        else:
            # print ('Program wrong 1')
            log = open(r'./wronglog.ini','a')
            log.write('Program wrong 1\n')
            log.close()
    def registerBC():
        _1_3_addUserUIM.addUserUI()
    
    validbt = Button(frame, text = '登录', command = loginBC).grid(row = 2,\
        column = 1, sticky = E, padx = 20, pady = 10)
    registerbt = Button(frame, text = '注册', command = registerBC).grid(row = 2,\
        column = 0, sticky = W, padx = 20, pady = 10)
    root.mainloop()

if __name__ == '__main__':
    log = open(r'./wronglog.ini','w')
    log.write('Program Start\n')
    log.close()
    loginSubUI()


