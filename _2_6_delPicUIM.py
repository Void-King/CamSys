import os
import tkinter as tk
import sys
def delPicUI(save_path):
    root = tk.Tk()
    root.title('Del')
    try:
        root.iconbitmap('./pic/Cam.ico')
    except:
        # print ('Program wrong 1')
        log1 = open(r'./wronglog.ini', 'a')
        log1.write('Program wrong 1\n')
        log1.close()
    root.resizable(0, 0)
    label = tk.Label(root, text = '是否删除保存的图片和视频?')
    label.pack(padx = 20, pady = 10)
    frame = tk.Frame(root)
    frame.pack()
    def del_file():
        nonlocal save_path
        # print (save_path)
        try:
            ls = os.listdir(save_path)
            for i in ls:
                c_path = os.path.join(save_path, i)
                os.remove(c_path)
        except:
            log = open(r'./wronglog.ini', 'a')
            log.write('Program wrong 6\n')
            log.close()
        sys.exit(0)
    def quitconf():
        sys.exit(0)
    confbt = tk.Button(frame, text = '删除', command = del_file)
    confbt.grid(row = 0, column = 0, padx = 10, pady = 5)
    cansbt = tk.Button(frame, text = '保留', command = quitconf)
    cansbt.grid(row = 0, column = 1, padx = 10, pady = 5)
    root.protocol("WM_DELETE_WINDOW", quitconf)
    root.mainloop()