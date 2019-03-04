#coding=utf-8
import itchat, time, sys, re, requests
from itchat.content import *
from bs4 import BeautifulSoup

 
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
            danjialist = []
            URL = 'https://n.cbg.163.com/?serverid=52'
            html = requests.get(URL).text
            soup = BeautifulSoup(html, 'html.parser')

            for i in soup.find_all("td",class_="c_Red"):
              i = i.get_text().strip()
              danjialist.append(i)
              i = '\n'+i
              list.append(i)
            print(''.join(list[0:10]))

            danjia = danjialist[1::2]
            dan = 0.00
            for d in danjia:
              d = d.strip('元/万文')
              d = float(d)
              dan = dan + d
            dan = float('%.2f' % dan)
            average = dan / len(danjia)
            jiage = float('%.2f' % average)
            print("约等:",jiage,"元")
            xianxia = average * 0.95
            xianxia = float('%.2f' % xianxia)
            print("线下:",xianxia,"元")

            page_total = soup.find("span",class_="page-total")
            pages = page_total.get_text()
            times = int(pages)
            total = 0
            for page in range(times+1):
              page = str(page)
              url = URL+'&page='+page
              html = requests.get(url).text
              soup = BeautifulSoup(html, 'html.parser')
              tong = soup.find_all("p",text=re.compile(r'(\d)+万'))
              for i in tong:
                i = (i.text.strip('万'))
                i = int(i)
                total = total + i
            print('铜总量:',total,"万",",总价值",total*jiage,"RMB")
            f = open("history.txt", "a+", encoding="utf-8")
            shijian = time.strftime('%Y-%m-%d %H:%M:%S')
            total = str(total)
            jiage = str(jiage)
            history = shijian+' '+total+' '+jiage
            f.write(history+'\n')           
            f.close()
            '''
            msg.user.send(u'%s \n 约等于:%s元 线下:%s元 \n 铜总量:%s万 \n 总价值:%sRMB' % (
             ''.join(list[0:10]),jiage,xianxia,total,total*jiage))
            '''
        if msg.isAt:
            if msg.actualNickName == '秦琪（广陵散人）':
                msg.user.send(u'@%s\u2005 %s' % (
                    msg.actualNickName, '我可爱的徒弟,你要加油哦 คิดถึง '))

             
 
 
 
itchat.auto_login(enableCmdQR=2,hotReload=True)
itchat.run()
