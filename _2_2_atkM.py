import requests
import time
import os
import sys
import threading

#每隔一小时从服务器获取accesstoken（每两小时失效）
def get_atk(atktime, imgts):
    while 1:
        url_token = 'https://api.weixin.qq.com/cgi-bin/token?'
        res = requests.get(url=url_token,params={
                "grant_type": 'client_credential',
                'appid':'wx2491724892232136',# 这里填写上面获取到的appID
                'secret':'5fb55edfbf0f94fa06dbc78449260045',# 这里填写上面获取到的appsecret
                }).json()
        token = res.get('access_token')
        # atkf = open(r'./atk.ini','w')
        # atkf.write(token)
        atktime[1] = token
        # print (atktime[1])
        log = open(r'./wronglog.ini','a')
        log.write(atktime[1] + '\n')
        log.close()
        # atkf.close()
        for i in range(0,3600):
            # print (i)
            if i == 1800:
                if len(imgts) == 2:
                    imgts[1] = None
                    # print (imgts)
            if atktime[0] == -1:
                sys.exit(0)
            atktime[0] -= 1
            time.sleep(1)
        atktime[0] = 3600
        # break
