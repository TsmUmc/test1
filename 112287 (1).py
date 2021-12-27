#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install twstock


# In[2]:


twstock -b 2330 6223


# In[3]:


import twstock


# In[4]:


twstock -b 2330 6223


# In[5]:


twstock -s 2330 6223


# In[6]:


s 2330 6223


# In[7]:


import pandas as pd
import numpy as np
import talib
import matplotlib.pyplot as plt
import pybacktest


# In[8]:


pip install tabil


# In[9]:


pip install talib


# In[10]:


plt.rcParams.update({
    'font.family': ['Microsoft JhengHei'],
    'figure.autolayout': True,
    'axes.unicode_minus': True,
    'savefig.dpi': 100,
    'figure.dpi': 100


# In[11]:


import csv
fn='STOCK_DAY_ALL_20211122.csv'
with open(fn,encoding='utf8')as csvFile:
    csvReader=csv.reader(csvFile)
    listReport=list(csvReader)
print(listReport)  


# In[12]:


import csv
fn='STOCK_DAY_ALL_20211122.csv'


# In[13]:


print(listReport)  


# In[14]:


pip install yfinance


# In[15]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
plt.style.use('fivethirtyeight')


# In[16]:


df.tail(15)


# In[17]:


#股票代號
stock_no='2330.TW'
#起始日期
start_date='2019-01-01'
#下載資料
df=yf.download(stock_no,start=start_date)


# In[18]:


df.tail(15)


# In[19]:


#畫出歷史股價走勢圖
#不能直接使用中文字型，所以用英文代替
#如何使用中文字型，請參考之前的文章或自行google
plt.figure(figsize=(12.2,4.5))
plt.plot(df['Close'], label='Close')
plt.title('Close Price History')
#字斜45度角
plt.xticks(rotation=45)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()


# In[20]:


#Calculate the MACD and Signal line indicators
#Calculate the short term exponential moving average (EMA)
#指數移動平均線
ShortEMA=df.Close.ewm(span=12,adjust=False).mean()
#Calculate the long term exponential moving average (EMA)
LongEMA=df.Close.ewm(span=26,adjust=False).mean()
#Calculat the MACD line
MACD=ShortEMA-LongEMA
#Calculat the Signal line
signal=MACD.ewm(span=9,adjust=False).mean()


# In[21]:


#畫圖
plt.figure(figsize=(12.2,4.5))
plt.xticks(rotation=45)
plt.plot(df.index , MACD, label='2330 MACD', color='red')
plt.plot(df.index , signal, label='Signal', color='Blue')
plt.legend(loc='upper left')
plt.show()


# In[22]:


df['MACD']=MACD
df['Signal Line']=signal
df.head()


# In[23]:


# create a funtion to signal when to buy and sell an asset
#買賣點的判斷，這只是一個示範，並不能實際用於買賣股票!!!
def Buy_Sell(signal):
  Buy=[]
  Sell=[]
  flag=-1

  for i in range(0,len(signal)):
    if signal['MACD'][i] > signal['Signal Line'][i]:
      Sell.append(np.nan)
      if flag !=1:
        Buy.append(signal['Close'][i])
        flag=1
      else:
        Buy.append(np.nan)
    elif signal['MACD'][i] < signal['Signal Line'][i]:
      Buy.append(np.nan)
      if flag !=0:
        Sell.append(signal['Close'][i])
        flag=0
      else:
        Sell.append(np.nan)
    else:
      Buy.append(np.nan)
      Sell.append(np.nan)
 
  return(Buy,Sell)
      


# In[24]:


a=Buy_Sell(df)
df['Buy_Signal_Price']=a[0]
df['Sell_Signal_Price']=a[1]


# In[25]:


df.tail(15)


# In[26]:


#Visually show the stock buy and sell signal
plt.figure(figsize=(12.2,4.5))
# ^ = shift + 6
plt.scatter(df.index,df['Buy_Signal_Price'],color='red', label='Buy',marker='^',alpha=1)
#小寫的v
plt.scatter(df.index,df['Sell_Signal_Price'],color='green', label='Sell',marker='v',alpha=1)
plt.plot(df['Close'], label='Close Price', alpha=0.35)
plt.title('Close Price Buy & Sell Signals')
#字斜45度角
plt.xticks(rotation=45)
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.show()


# In[ ]:




