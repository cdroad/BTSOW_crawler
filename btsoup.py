#!/usr/bin/python3 
# -*- coding: utf-8 -*-

import requests;
from bs4 import BeautifulSoup
urls=[]
key='母狗'
url = 'https://btsow.shop/search/' + key
hash_head = 'magnet:?xt=urn:btih:'
#对内容进行编码
html = requests.get(url);
html.encoding = html.apparent_encoding
content = html.text
soup = BeautifulSoup(content, 'html.parser');
data_div = soup.find_all("div","data-list")


#提取出所有list里的href值
def tiqu():
    for n in text:
        urls.append(n['href'])
        #拿到大小日期
        b = n.find_all('div',class_='col-xs-12 size-date visible-xs-block')
        c = b[0].get_text()
        #拿到标题
        title = n['title']
        #切片提取hash
        l_hash = str(n['href'])
        tiqu_hash = l_hash[32:]
        jiehe_hash = hash_head + tiqu_hash
        #print(title + '\n' + l_hash[32:n] + '\n' + c)
        print(title + '\n' + c + '\n' + jiehe_hash + '\n' + '------------------------------------------------------------------------------------------')


if(len(data_div) == 0):
   print("没有找到内容")
else:
    for n in data_div:
        text = n.find_all('a') 
    tiqu()




    


