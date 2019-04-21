import tkinter as tk
from tkinter import *
import cv2
from PIL import Image,ImageTk
import threading
import sys
import os
import time

import _2_2_atkM
import _2_3_moveDetM
import _2_6_delPicUIM
import _2_7_recordM

atktime = [3600,'Null']
sz = []

def camUI(save_path, wxid):
    global atktime
    imgts = [] # 0 是实时帧图像画面 1是检测背景对比图
    recordFlag = [False, False]
    funcFlag = False

    class thread1 (threading.Thread):
        def __init__(self, atktime, imgts):
            threading.Thread.__init__(self)
            self.atktime = atktime
            self.imgts = imgts
        def run(self):
            _2_2_atkM.get_atk(atktime, imgts)
    class thread2 (threading.Thread):
        def __init__(self, atktime):
            threading.Thread.__init__(self)
            self.atktime = atktime
        def run(self):
            camUIThread(atktime)
    class thread3 (threading.Thread):
        def __init__(self, atktime, imgts, save_path, wxid, recordFlag, sz):
            threading.Thread.__init__(self)
            self.atktime = atktime
            self.imgts = imgts
            self.save_path = save_path
            self.wxid = wxid
            self.recordFlag = recordFlag
            self.sz = sz
        def run(self):
            _2_7_recordM.record(imgts, atktime, save_path, wxid, recordFlag, sz)

    def camUIThread(atktime):
        global sz
        # 摄像头
        camera = cv2.VideoCapture(1)
        suc, img = camera.read()
        background = None
        if suc:
            sz.append((int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
                        int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))))
            imgts.append(img)
            imgts.append(background)
        else:
            # print ('Program Wrong 4') #摄像头读取失败
            log = open(r'./wronglog.ini','a')
            log.write('Program wrong 4\n')
            log.close()
        root = tk.Tk()
        root.iconbitmap('./pic/Cam.ico')
        root.resizable(0, 0)
        root.title('Cam')
        vidlabel = Label(root, text = 'Cam Not Found')
        vidlabel.pack(padx = 10, pady = 10)
        frame = tk.Frame(root)
        frame.pack(pady = 5)
        i = 0
        def video_change():
            nonlocal vidlabel, funcFlag, i, imgts, recordFlag
            global imagetk #PIL更新图片保持引用?
            suc, img = camera.read()
            if funcFlag:
                _2_3_moveDetM.moveDet(img, imgts, recordFlag)
                # 检测功能
            else:
                imgts[0] = img
            
            if suc:
                image1 = cv2.cvtColor(imgts[0], cv2.COLOR_BGR2RGBA)
                image2 = Image.fromarray(image1)
                imagetk = ImageTk.PhotoImage(image2)
                # vidlabel.imagetk = imagetk
                vidlabel.configure(image = imagetk)
                # if recordFlag[1]:
                #     print ('facedet')
                #     recordFlag[1] = False
                vidlabel.after(10, video_change)
            else:
                # print ('Program Wrong 4') #摄像头读取失败
                log = open(r'./wronglog.ini','a')
                log.write('Program wrong 4\n')
                log.close()
        def endProgram():
            nonlocal atktime, camera, root, save_path
            atktime[0] = -1
            _2_6_delPicUIM.delPicUI(save_path)
            camera.release()
            cv2.destroyAllWindows()
            sys.exit(0)
        
        redsignimg = tk.PhotoImage(file = './pic/red.png')
        gresignimg = tk.PhotoImage(file = './pic/green.png')

        def startFuc():
            nonlocal retimeentry, startbt, signlabel2, funcFlag
            # print ('开始')
            try:
                i = int(retimeentry.get())
            except:
                retimeentry.delete(0, END)
                retimeentry.insert(0, '请重新输入(纯数字整数)')
            flag = True
            while flag:
                if i <= 0:
                    retimeentry.delete(0, END)
                    retimeentry.insert(0, '0')
                    flag = False
                else:
                    # 定时器
                    for j in range(0,6):
                        time.sleep(0.1)
                        retimeentry.update()
                    i -= 1
                    retimeentry.delete(0, END)
                    retimeentry.insert(0, str(i))
                    retimeentry.update()
            funcFlag = True
            startbt.configure(text = '停止')
            startbt.configure(command = stopFuc)
            signlabel2.configure(image = gresignimg)
        def stopFuc():
            nonlocal suc, retimeentry, startbt, signlabel2, funcFlag, imgts
            funcFlag = False
            if suc:
                imgts[1] = None
            # i = int(retimeentry.get())
            # print (i)
            startbt.configure(text = '开始')
            startbt.configure(command = startFuc)
            signlabel2.configure(image = redsignimg)

        

        signlabel1 = Label(frame, text = '移动检测功能状态:')
        signlabel1.grid(row = 0, column = 0, sticky = E, padx = 0, pady = 5)
        signlabel2 = Label(frame, image = redsignimg)
        signlabel2.grid(row = 0, column = 1, sticky = E, padx = 3, pady = 5)
        retimelabel1 = Label(frame, text = '倒计时')
        retimelabel1.grid(row = 0, column = 2, sticky = E, padx = 2, pady = 5)
        retimeentry = Entry(frame)
        retimeentry.grid(row = 0, column = 3, sticky = E, padx = 0, pady = 5)
        retimeentry.insert(0, '0')
        retimelabel2 = Label(frame, text = '秒')
        retimelabel2.grid(row = 0, column = 4, sticky = E, padx = 2, pady = 5)

        startbt = Button(frame, text = '开始', command = startFuc)
        startbt.grid(row = 0, column = 5, sticky = W, padx = 20, pady = 5)
        endbt = Button(frame, text = '退出', command = endProgram).grid(row = 0,\
                column = 6, sticky = W, padx = 20, pady = 5)
        root.protocol("WM_DELETE_WINDOW", endProgram)

        atklabel = Label(frame, text = 'ATK刷新时间:00:00')
        atklabel.grid(row = 0, column = 7, sticky = E, padx = 20, pady = 5)
        def atktimeupdate():
            nonlocal atktime
            showtime = 'ATK刷新时间:'
            if (0 <= int(atktime[0]) // 60 <= 9):
                showtime += '0'
            showtime += str(int(atktime[0]) // 60) + ':'
            if (int(atktime[0]) - 60 * (int(atktime[0]) // 60) <= 9):
                showtime += '0'
            showtime += str(int(atktime[0]) - 60 * (int(atktime[0]) // 60))
            atklabel.configure(text = showtime)
            atklabel.after(100,atktimeupdate)
        if suc:
            video_change()
            atktimeupdate()
        root.mainloop()

    th1 = thread1(atktime, imgts)
    th2 = thread2(atktime)
    th3 = thread3(imgts, atktime, save_path, wxid, recordFlag, sz)
    th1.start()
    th2.start()
    th3.start()

# camUI('./pic/movesave/', '123')