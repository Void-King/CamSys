# -*- coding: utf-8 -*-

# filename: handle.py



import hashlib

import web

import lxml.etree 

from lxml.etree import *

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

        msgType=xml.find("MsgType").text

        fromUser=xml.find("FromUserName").text

        toUser=xml.find("ToUserName").text

        return render.reply_text(fromUser,toUser,456456,content)