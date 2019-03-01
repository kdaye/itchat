#coding=utf-8
import itchat, time, sys
from itchat.content import *
 
from bs4 import BeautifulSoup
import requests
 
def group_id(name):
  df = itchat.search_chatrooms(name=name)
  return df[0]['UserName']
'''
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def _(msg):
    print('%s: %s' % (msg.type, msg.text))

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def download_files(msg):
    msg.download('files/'+msg.actualNickName+msg.fileName)
   
    itchat.send('@%s@%s' % (
            'img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']),
            msg['FromUserName'])
'''
         
 
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    item = group_id(u'逆水寒 - 长乐')
    if msg['FromUserName'] == item or msg['ToUserName'] == item:
        print(msg.actualNickName,':',msg.text)
        if msg.text == '金价':
            list = []
            URL = 'https://n.cbg.163.com/?serverid=52'
            html = requests.get(URL).text
            soup = BeautifulSoup(html, 'html.parser')
            for i in soup.find_all("td",class_="c_Red"):
                list.append(i.get_text())
            msg.user.send(''.join(list))
        if msg.isAt:
            if msg.actualNickName == '秦琪（收小弟）':
                msg.user.send(u'@%s\u2005 %s' % (
                    msg.actualNickName, '我可爱的徒弟,你要加油哦 คิดถึง '))
            if msg['ActualUserName'] == '@235c7d8b2b7dbe62ec357a8836eb4b02fe2fd21634a733a155c5cea3fd7a7979':
                msg.user.send(u'biubiubiu')
             
 
 
 
itchat.auto_login(enableCmdQR=2,hotReload=True)
itchat.run()
