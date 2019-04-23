# -*- coding: utf-8 -*-



# filename: handle.py







import hashlib



import web



import lxml.etree 



from lxml.etree import *

import pymysql
import os

def sql_sent(sqle):
    db = pymysql.connect("123.207.117.11","wxuser","KeXncyAj","wxuserdb")
    cursor = db.cursor()
    cursor.execute(sqle)
    if sqle[:6] == 'SELECT':
        data = cursor.fetchall()
        return data
    elif sqle[:6] == 'INSERT':
        db.commit()
    elif sqle[:6] == 'UPDATE':
        db.commit()
    else:
        print('Program Wrong')
    db.close()


render = web.template.render("templates")



class Handle(object):



    def GET(self):



        try:



            data = web.input()



            if len(data) == 0:



                return "hello, this is handle view"



            signature = data.signature



            timestamp = data.timestamp



            nonce = data.nonce



            echostr = data.echostr



            token = "nnn111"







            list = [token, timestamp, nonce]



            list.sort()



            sha1 = hashlib.sha1()



            list2 = ''.join(list)



            sha1 = hashlib.sha1()



            sha1.update(list2.encode('utf-8'))



            hashcode = sha1.hexdigest()



            print ("handle/GET func: hashcode, signature: ", hashcode, signature)



            if hashcode == signature:



                return echostr



            else:



                return ""



        except (Exception, Argument):



            return Argument



    def POST(self):        



        str_xml = web.data()



        xml =  lxml.etree.XML(str_xml)



        content="更新连接成功！"



        msg = xml.find("Content").text



        msgType=xml.find("MsgType").text



        fromUser=xml.find("FromUserName").text



        toUser=xml.find("ToUserName").text
        sql = '''UPDATE `user_list`
                SET `times` = '0'
                WHERE `wxid` = \'''' + str(fromUser) + '''\';
                '''
        sql_sent(sql)
        
        if str(msg) == 'tp':
            sql = '''UPDATE `user_list`
                    SET `request` = '1'
                    WHERE `wxid` = \'''' + str(fromUser) + '''\';
                    '''
            sql_sent(sql)
        if str(msg) == 'sp':
            sql = '''UPDATE `user_list`
                    SET `request` = '2'
                    WHERE `wxid` = \'''' + str(fromUser) + '''\';
                    '''
            sql_sent(sql)
        if str(msg)[0:2] == 'zt':
            c = 0
            try:
                c = int(str(msg)[2:])
                if 0 < c <= 90:
                    # print (int(str(msg)[2:]))
                    sql = '''UPDATE `user_list`
                            SET `request` = \'3''' + str(int(str(msg)[2:])) + '''\'
                            WHERE `wxid` = \'''' + str(fromUser) + '''\';
                            '''
                    sql_sent(sql)
                    content = '系统已暂停' + str(int(str(msg)[2:])) + '分钟'
                else:
                    content = '请输入大于0小于等于90的整数(分钟)'
            except:
                pass
        if str(msg) == 'ks':
            sql = '''UPDATE `user_list`
                    SET `request` = '4'
                    WHERE `wxid` = \'''' + str(fromUser) + '''\';
                    '''
            sql_sent(sql)
            content = '系统开始继续运行'
        # print (fromUser)
        # print (data)

        return render.reply_text(fromUser,toUser,456456,content)