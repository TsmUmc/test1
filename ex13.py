# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:50:28 2021

@author: Administrator
"""


import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split

d=datasets.load_diabetes()
print(d.keys())

x=pd.DataFrame(d.data,columns=d.feature_names)
# x1=x[['age','sex','bmi','bp']]
print(x.head())

t=pd.DataFrame(d.target,columns=['MEDV'])
print(t.head())

y=t['MEDV']

# xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3,random_state=100)

lm=LinearRegression ()
lm.fit(x,y)

pt=lm.predict(x)
print(pt[0:5])


coef=pd.DataFrame(d.feature_names,columns=['features'])
coef['estimatedcofficients']=lm.coef_
print(coef)
# pr=lm.predict()

mse=np.mean((y-pt)**2)
print('mse:',mse)
print('r^2:',lm.score(x,y))



plt.scatter(y,pt)
plt.show()
