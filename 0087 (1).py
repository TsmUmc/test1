#!/usr/bin/env python
# coding: utf-8

# In[3]:


import re
import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[4]:


#標頭檔
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
#網址
#url='https://www.pesobility.com/stock/blue-chips'
url='https://www.pesobility.com/stock'


# In[6]:


#標題檔,investing有擋爬蟲
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
#網址
base_url='https://hk.investing.com/equities/philippines'
#https://cn.investing.com/equities/ayala-corp


# In[7]:


#抓取網頁
res = requests.get(base_url, headers=headers)
#轉成 BeautifulSoup
soup=BeautifulSoup(res.text,'lxml')
#印出，內容太多就省略
#soup


# In[8]:


#選取網頁元素
results = soup.find_all('td', attrs={'class':'bold left noWrap elp plusIconTd'})
#印出，內容太多就省略
#results
#資料筆數
len(results)


# In[9]:



#印其中一筆
print(results[1])


# In[10]:


#內容測試
print(results[1].find('a'))
print(results[1].find('a').text)
print(results[1].find('a')['href'])


# In[11]:



link={}
base_url='https://hk.investing.com'
for  i in results:
    #公司名稱
    title=i.find('a').text
    #網頁連結
    getlink=i.find('a')['href']
    #完整的網頁連結
    url='{}'.format(base_url+getlink)
    #加到字典裡
    link[title]=url


# In[12]:


#印出字典內容
link


# In[13]:


#印出各別公司的網頁連結
print(link['Bloomberry Resorts'])


# In[14]:


url2='https://hk.investing.com/equities/dmci-holdings'
res2 = requests.get(url2, headers=headers)
soup2=BeautifulSoup(res2.text,'lxml')
#印出，內容太多就省略
#soup2


# In[15]:


#抓取網頁元素
results2 = soup2.find_all("div", {"class": "clear overviewDataTable overviewDataTableWithTooltip"})
results2


# In[16]:


for i in results2:
    print(i.text)


# In[17]:



spans = soup2.find("div", {"class": "clear overviewDataTable overviewDataTableWithTooltip"}).find_all('span', attrs={'class':'float_lang_base_1'})
spans2 = soup2.find("div", {"class": "clear overviewDataTable overviewDataTableWithTooltip"}).find_all('span', attrs={'class':'float_lang_base_2'})
for span in spans:
    print(span.text)


# In[18]:


import pandas as pd  
import numpy as np  
from pandas_datareader import data


# In[19]:


sp500 = data.DataReader('^GSPC', 'yahoo',start='1/1/2000') 


# In[20]:


sp500.head()


# In[21]:


sp500['Close'].plot(grid=True,figsize=(8,5))


# In[22]:


sp500['42d'] = np.round(sp500['Close'].rolling(window=42).mean(),2)  
sp500['252d'] = np.round(sp500['Close'].rolling(window=252).mean(),2) 


# In[23]:


sp500[['Close','42d','252d']].plot(grid=True,figsize=(8,5)) 


# In[24]:


sp500['42-252'] = sp500['42d'] - sp500['252d'] 


# In[25]:


X = 50  
sp500['Stance'] = np.where(sp500['42-252'] > X, 1, 0)  
sp500['Stance'] = np.where(sp500['42-252'] < -X, -1, sp500['Stance'])  
sp500['Stance'].value_counts() 


# In[26]:


sp500['Stance'].plot(lw=1.5,ylim=[-1.1,1.1]) 


# In[27]:


sp500['Market Returns'] = np.log(sp500['Close'] / sp500['Close'].shift(1))  
sp500['Strategy'] = sp500['Market Returns'] * sp500['Stance'].shift(1) 


# In[28]:


sp500[['Market Returns','Strategy']].cumsum().plot(grid=True,figsize=(8,5)) 


# In[ ]:




