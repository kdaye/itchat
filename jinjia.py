#coding=utf-8
from bs4 import BeautifulSoup
import requests

           list = []
            URL = 'https://n.cbg.163.com/?serverid=52'
            html = requests.get(URL).text
            soup = BeautifulSoup(html, 'html.parser')
            for i in soup.find_all("td",class_="c_Red"):
                list.append(i.get_text())
            print(''.join(list))
            page_total = soup.find_all("span",class_="page-total")
            print(page_total)
