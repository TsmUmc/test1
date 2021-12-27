#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import talib
import matplotlib.pyplot as plt
import pybacktest


# In[3]:



#這個範例使用 google colab的服務
#在colab 下載以下套件
get_ipython().system('pip install yfinance')


# In[4]:


#credit https://youtu.be/kz_NJERCgm8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
plt.style.use('fivethirtyeight')


# In[22]:


'''
如果不能安裝 yfinance
就到 https://finance.yahoo.com/quote/2303.TW/history?p=2303.TW
下載歷史股價的csv檔
'''
#股票代號
stock_no='2303.TW'
#起始日期
start_date='2019-01-01'
#下載資料
df=yf.download(stock_no,start=start_date)


# In[23]:


df.tail(15)


# In[24]:


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


# In[11]:


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


# In[25]:


#畫圖
plt.figure(figsize=(12.2,4.5))
plt.xticks(rotation=45)
plt.plot(df.index , MACD, label='2303 MACD', color='red')
plt.plot(df.index , signal, label='Signal', color='Blue')
plt.legend(loc='upper left')
plt.show()


# In[26]:



df['MACD']=MACD
df['Signal Line']=signal
df.head()


# In[27]:


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


# In[28]:


a=Buy_Sell(df)
df['Buy_Signal_Price']=a[0]
df['Sell_Signal_Price']=a[1]


# In[29]:


df.tail(15)


# In[30]:



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




