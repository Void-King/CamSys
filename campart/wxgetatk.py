import requests
import time
import os
#每隔一小时从服务器获取accesstoken（每两小时失效） 并导出到atk.ini
def get_atk(atktime):
    while 1:
        url_token = 'https://api.weixin.qq.com/cgi-bin/token?'
        res = requests.get(url=url_token,params={
                "grant_type": 'client_credential',
                'appid':'wx2491724892232136',# 这里填写上面获取到的appID
                'secret':'5fb55edfbf0f94fa06dbc78449260045',# 这里填写上面获取到的appsecret
                }).json()
        token = res.get('access_token')
        try:
            os.remove(r'./cam1/atk.ini')
        except:
            pass
        atkf = open(r'./cam1/atk.ini','x')
        atkf.write(token)
        atkf.close()
        for i in range(0,3600):
            # print (i)
            atktime[0] -= 1
            time.sleep(1)
        atktime[0] = 3600
        # break
        #time.sleep(3600)#3600秒 每隔一小时更新一次
#导入atk到程序中
def use_atk():
    token = "null"
    while token == "null":
        try:
            atkf = open(r'./cam1/atk.ini','r')
            token = atkf.readline()
            atkf.close()
        except:
            print ("not exist")
            time.sleep(2)
            continue
    return token