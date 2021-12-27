#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from io import StringIO
import datetime
import os


# In[3]:


url = "https://isin.twse.com.tw/isin/class_main.jsp?owncode=&stockname=&isincode=&market=1&issuetype=1&industry_code=&Page=1&chklike=Y"
response = requests.get(url)
listed = pd.read_html(response.text)[0]
listed.columns = listed.iloc[0,:]
listed = listed[["有價證券代號","有價證券名稱","市場別","產業別","公開發行/上市(櫃)/發行日"]]
listed = listed.iloc[1:]
listed


# In[4]:


stock_1 = listed["有價證券代號"]
stock_num = stock_1.apply(lambda x: str(x) + ".TW")
stock_num


# In[7]:


##讀寫成csv檔
def stock_data(stock_id,time_start,time_end) :
    days = 24 * 60 * 60    #一天有86400秒 
    initial = datetime.datetime.strptime( '1970-01-01' , '%Y-%m-%d' )
    start = datetime.datetime.strptime( time_start , '%Y-%m-%d' )
    end = datetime.datetime.strptime( time_end, '%Y-%m-%d' )
    period1 = start - initial
    period2 = end - initial
    s1 = period1.days * days
    s2 = period2.days * days
    url = "https://query1.finance.yahoo.com/v7/finance/download/" + stock_id + "?period1=" + str(s1) + "&amp;period2=" + str(s2) + "&amp;interval=1d&amp;events=history&amp;includeAdjustedClose=true"
    response = requests.get(url)
    df = pd.read_csv(StringIO(response.text),index_col = "Date",parse_dates = ["Date"])
    address = r"C:\Users\adsad\OneDrive\Desktop\stock\\" + stock_id + ".csv"
    if  os.path.isfile(address):
        df_new = pd.read_csv(address,index_col = "Date",parse_dates = ["Date"])
        if time_start not in df_new.index:
            df_new = df_new.append(df)
            df_new.to_csv(address,encoding='utf-8')
            print("已更新到最新資料")
        else:
            print("已是最新資料，無需更新")
    else:
        df.to_csv(address,encoding='utf-8')
        print("此為新資料，已創建csv檔")


# In[9]:


time_start = "2000-01-01"
time_end = "2020-12-23"
for i in stock_num :   
    try:
        stock_data(i, time_start,time_end)
        print(i + "successful")
    except:
        print(i + "fail")


# In[10]:


import requests
import pandas as pd
from io import StringIO


# In[11]:


url = "https://query1.finance.yahoo.com/v7/finance/download/2330.TW?period1=1572420723&period2=1604043123&interval=1d&events=history&includeAdjustedClose=true"
response = requests.get(url)
response.text


# In[13]:


import requests
url = "https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID=2330"
res = requests.get(url)
res.encoding = "utf-8"
res.text
res.text


# In[14]:


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
res = requests.get(url,headers = headers)
res.encoding = "utf-8"
res.text


# In[15]:


from bs4 import BeautifulSoup
soup = BeautifulSoup(res.text,"lxml")
data = soup.select_one("#txtFinDetailData")
data


# In[16]:


import pandas as pd
dfs = pd.read_html(data.prettify())
df = dfs[0]
df


# In[18]:


df.columns = df.columns.get_level_values(1)
df


# In[ ]:




