# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 15:12:14 2021

@author: Administrator
"""

import numpy as np
import pandas as pd

# x=np.random.rand(100,4)
# y=np.random.randn(100,4)


# df1=pd.DataFrame(x,index=pd.date_range('3/1/20',periods=100),
#                     columns=list('abcd'))

# df2=pd.DataFrame(y,index=pd.date_range('3/1/20',periods=100),
#                     columns=list('abcd'))
df=pd.DataFrame(np.random.randn(500,3),columns=list('xyz'),
                index=pd.date_range('1/1/2019',periods=500))


# df1.plot()
# df2.plot()

df=df.cumsum()
df.plot().set_ylabel('value',fontsize=12)

df2=pd.DataFrame(np.random.rand(5,3),columns=['a','b','c'])
df2.plot(kind='bar',fontsize=12,stacked=True)
# df3=df1.cumsum()
# df4=df2.cumsum()
# df3.plot()
# df4.plot()


