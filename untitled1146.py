# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:38:02 2021

@author: Administrator
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
from selenium.webdriver.support.ui import Select
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

d=webdriver.Chrome('chromedriver')
# h3=os.path.abspath('SeleniumTest.html')
d.implicitly_wait(5)
d.get('https://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1')
#onetrust-accept-btn-handler
d.find_element_by_css_selector('#onetrust-accept-btn-handler').click()

p=True
pn=1
while p:
    s=BeautifulSoup(d.page_source,'lxml')
    t=s.select_one('body > main > div > div > div.row > div > div > nba-stat-table > div.nba-stat-table')
    df=pd.read_html(str(t))
    df[0].to_csv('test.csv')
    # try:
    #     next=d.find_element_by_xpath('/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/a[2]')
    #     next.click()
        
# i=d.find_elements_by_css_selector('li')
# for j in i:
#     print(j.text)
# print(d.title)
# s=BeautifulSoup(d.page_source,'lxml')
# fp=open('index.html','w',encoding='utf8')
# fp.write(s.prettify())
# # h=d.page_source
# # print(h)
# # time.sleep(3)
# .close()
d.quit()
# l=[]

# d=webdriver.Chrome('chromedriver')
# # h3=os.path.abspath('SeleniumTest.html')
# d.implicitly_wait(5)
# d.get('https://mops.twse.com.tw/mops/web/t163sb04')
# print(d.title)
# # d.find_element_by_id('TYPEK').click()

# # sy=Select(d.find_element_by_id('TYPEK'))
# # y='上市'
# # sy.select_by_value(y)
# while True:
#     sy=Select(d.find_element_by_id('year'))
#     y=input('輸入:')
#     print('wait')
#     sy.select_by_value(str(y))
    
# d.quit()

