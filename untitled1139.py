# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 15:26:57 2021

@author: Administrator
"""

import requests as rq
import csv
import pandas as pd

url='https://api.finmindtrade.com/api/v4/datalist'
r=rq.request('GET',url)
d=list(csv.reader(r.text.split()))
df=pd.DataFrame(d[1:len(d)-1])
df.index+=1
print(df)