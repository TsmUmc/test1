# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 09:41:21 2021

@author: Administrator
"""

import requests,os,urllib
import re
from bs4 import BeautifulSoup
import time
import random

ip=['223.96.90.216:8085','112.6.117.178:8085']
ip2=random.choice(ip)
print("Use",ip2)
 
# url='https://www.ptt.cc/bbs/NBA/index6506.html'
# deleted=BeautifulSoup("<a href='Deleted'>本文已刪除</a>",'lxml')
r2= requests.get('http://ip.filefab.com/index.php',
                 proxies={'http':'http://'+ip2})
bs=BeautifulSoup(r2.text,'lxml')
print(bs.find('h1',id='ipd').text.strip())

# for i in range(5011,5012):
#     url=url.format(i)
#     r=requests.get(url)
#     print(r.status_code)
# headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
r= requests.get(url,cookies={'over18':'1'})
print(r.status_code)
# +'searchShop.jsp?keyword=apple',headers=headers
if r.status_code==200:
    r.encoding='utf8'
    bs=BeautifulSoup(r.text,'lxml')
    tag_divs=bs.find_all('div',class_='r-ent')
    for tag in tag_divs:
        if tag.find('a'):
            tag_a=tag.find('a')
            # 
            print(tag_a['href'])
            print(tag_a.text)
            print(tag.find('div',class_='author').string)
            print(tag.find('div',class_='date').string)
else:
    print('error')
#     print(r.text)
# else:
#     print("error")
    
    
    
# for i in range(5000,5012):
#     url=url.format(i)
#     r=requests.get(url)
#     print(r.status_code)
#     time.sleep(3)
# bs=BeautifulSoup(r.text,'lxml')
# h2=bs.find_all('article-menu')

# h=requests.get(url)
# bs=BeautifulSoup(h.text,'lxml')
# # h2=bs.find_all('li','Pos(r)')
# p='pics'
# if not os.path.exists(p):
#     os.mkdir(p)
# a=bs.find_all('img')
# for l in a:
#     src=l.get('src')
#     attrs=[src]
#     for attr in attrs:
#         if attr!=None and('.jpg' in attr or '.png' in attr):
#             f=attr
#             f2=f.split('/'[-1])
#             try:
#                 i=urllib.request.urlopen(f)
#                 f3=open(os.path.join(p,f2),'wb')
#                 print('succeed')
#                 f.close()
#             except:
#                 print('not succeed')
# # x=1
# for i in h2:
#     con=i.find('a')
#     print(x,con,sep=".")
#     x=x+1

# print(h2.prettify())
# print(h2.head)
# print(h2.title.string)
# if h.status_code==200:
#     pattern=input('輸入字串:')
#     if pattern in h.text:
#         print('搜尋%s成功' % pattern)
#     else: print('搜尋%s失敗' % pattern)
        
#     n=re.findall(pattern,h.text)
#     if n !=None:
#         print('%s 出現 %d 次' %(pattern,len(n)))
        
#     else:
#         print('%s 出現 0 次' % pattern)
              
# else: 
#     print('fail')  
          
    