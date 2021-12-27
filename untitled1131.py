# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 09:47:20 2021

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

plt.rcParams['font.family']='Microsoft YaHei'
plt.rcParams['font.size']=12

pont_path='c:\Windows\Fonts\msjh.ttc'

# 
# x=np.array([1,2,3,4,5,2,3,0,3])
# # 
# y=[2,3,4,5,6]
# y2=x*x
# t1=['<2','<3','<4','<5']


x=['stock','sleep','rest']
y=[10,12,2]
c=['red','lightblue','pink']
explode=(0,0,0.1)

plt.pie(y,labels=x,colors=c,
        shadow= True,explode=explode,autopct='%1.1f%%')

# plt.figure(figsize=(8,4),facecolor='lightblue')

plt.axis('equal')
# plt.hist(x,y)
# price=[679,687,1000]
# v=[87,99,187]

# plt.bar(x,y,width=5,tick_label=t1,label='sample1')

# plt.subplot(211)
# plt.plot(x,y1,'b-')
# plt.subplot(212)
# plt.plot(x,y2,'r--')


# plt.plot(x,x,"r--",x,x**2,"bs",x,x**3,"g^")
# plt.plot(x,y,'ro',label='y=x*2')
# plt.legend()
# plt.text(1,10,'y=x*2')

# plt.xlim(-10,10)
# plt.ylim(-50,50)
# plt.grid()
# # 
# plt.title('價格')

# # 
# plt.xlabel('價')
# # 
# plt.ylabel('量',rotation=0,
#            ha='right')
# plt.xticks(np.arange(5),
#             ('','<=30','31~60','61~100',''))
# plt.yticks(np.arange(5),
#             ('','<25','25~50','51~87','>87'))
# plt.minorticks_on()

plt.show() 