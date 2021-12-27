# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 19:33:08 2021

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

l=[]

d=webdriver.Chrome('chromedriver')
# h3=os.path.abspath('SeleniumTest.html')
d.implicitly_wait(5)
d.get('https://tw.stock.yahoo.com/quote/2303.TW/technical-analysis')
print(d.title)

# while True:
#     sy=Select(drive.find_element_by_id("TYPEK"))
    
    
    
#     sy=Select(d.find_element_by_id('TYPEK'))
#     year=
#     year=input('輸入:')
#     sy.select_by_value(year)
    print('wait')
    sy.select_by_value(year)
s=BeautifulSoup(d.page_source,'lxml')
fp=open('index.html','w',encoding='utf8')
fp.write(s.prettify())
# # h=d.page_source
# # print(h)
# # time.sleep(3)
fp.close()
d.quit()

# h4=d.find_element_by_tag_name('h3')
# print(h4.text)
# p1=d.find_element_by_tag_name('p')
# print(p1.text)
# c=d.find_element_by_class_name('content')
# print(c.text)
# f=d.find_element_by_id('loginForm')
# print(f.tag_name)
# print(f.get_attribute('id'))
# c2=d.find_element_by_css_selector('body > h3')
# print(c.text)
# p5=d.find_element_by_link_text('Continue')
# print(p5.text)
# l=d.find_element_by_css_selector('#loginForm')
# print(l.text)
# u=d.find_elements_by_name('continue')
# for i in u:
    
#     print(i.get_attribute('type'))
    
# d.quit()


