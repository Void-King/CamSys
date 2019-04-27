import requests
# import _2_2_atkM
import os
def setm2user(wxid, atk, msg):
    url_msg ='https://api.weixin.qq.com/cgi-bin/message/custom/send?'
    body = '''
    {
        "touser":"''' + wxid + '''",
        "msgtype":"text",
        "text":
        {
            "content":"'''+ msg + '''"
        }
    }
    '''
    res = requests.post(url=url_msg,params = {
            'access_token':atk
            },data=body).json()
    # print(res)
    log = open(r'./wronglog.ini','a')
    log.write(str(res) + '\n')
    log.close()

def setp2user(wxid, atk, pic):
    url = "https://api.weixin.qq.com/cgi-bin/media/upload?"
    files = {'file':(open(pic,'rb'))}
    res = requests.post(url=url,params = {
            'access_token':atk, 
            'type':'image'                                                                                          
            },files=files)
    picid = res.json()
    picid = picid.get('media_id')
    # print (picid)
    log = open(r'./wronglog.ini','a')
    log.write(str(picid) + '\n')
    log.close()
    url ='https://api.weixin.qq.com/cgi-bin/message/custom/send?'
    body = '''
    {
        "touser":"''' + wxid + '''",
        "msgtype":"image",
        "image":
        {
            "media_id":"''' + picid + '''"
        }
    }
    '''
    res = requests.post(url=url,params = {
            'access_token':atk
            },data=body).json()
    # print(res)
    log = open(r'./wronglog.ini','a')
    log.write(str(res) + '\n')
    log.close()

def setv2user(wxid, atk, pic, vid):
    url = "https://api.weixin.qq.com/cgi-bin/media/upload?"
    files = {'file':(open(pic,'rb'))}
    res = requests.post(url=url,params = {
            'access_token':atk, 
            'type':'image'                                                                                          
            },files=files)
    picid = res.json()
    picid = picid.get('media_id')
    # print (picid)
    log = open(r'./wronglog.ini','a')
    log.write(str(picid) + '\n')
    log.close()

    files = {'file':(open(vid,'rb'))}
    res = requests.post(url=url,params = {
            'access_token':atk, 
            'type':'video'                                                                                          
            },files=files)
    vidid = res.json()
    vidid = vidid.get('media_id')
    # print (vidid)
    log = open(r'./wronglog.ini','a')
    log.write(str(vidid) + '\n')
    log.close()

    url ='https://api.weixin.qq.com/cgi-bin/message/custom/send?'
    body = '''
    {
        "touser":"''' + wxid + '''",
        "msgtype":"video",
        "video":
        {
            "media_id":"''' + vidid + '''"
            "thumb_media_id":"''' + picid + '''",
            "title":"Record Video",
            "description":"Record Video"
        }
    }
    '''
    res = requests.post(url=url,params = {
            'access_token':atk
            },data=body).json()
    # print(res)
    log = open(r'./wronglog.ini','a')
    log.write(str(res) + '\n')
    log.close()
# setm2user('o__Cr1Y4gVbFpJv18yUdHN7cr4RI', _2_2_atkM.use_atk(), '123')