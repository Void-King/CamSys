import requests

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
    print(res)

def setp2user(wxid, atk, pic):
    url = "https://api.weixin.qq.com/cgi-bin/media/upload?"
    files = {'file':(open(pic,'rb'))}
    res = requests.post(url=url,params = {
            'access_token':atk, 
            'type':'image'                                                                                          
            },files=files)
    picid = res.json()
    picid = picid.get('media_id')
    print (picid)
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
    print(res)

def setv2user(wxid, atk, pic, vid):
    url = "https://api.weixin.qq.com/cgi-bin/media/upload?"
    files = {'file':(open(pic,'rb'))}
    res = requests.post(url=url,params = {
            'access_token':atk, 
            'type':'image'                                                                                          
            },files=files)
    picid = res.json()
    picid = picid.get('media_id')
    print (picid)

    files = {'file':(open(vid,'rb'))}
    res = requests.post(url=url,params = {
            'access_token':atk, 
            'type':'video'                                                                                          
            },files=files)
    vidid = res.json()
    vidid = vidid.get('media_id')
    print (vidid)

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
    print(res)