# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 14:05:43 2021

@author: Administrator
"""


import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing,linear_model


b=datasets.load_breast_cancer()
print(b.keys())

l=preprocessing.LabelEncoder()
# e=l.fit_transform(b['traget'])

# x=pd.DataFrame([l,b])
#                 # ['SexCode'],t['Age']]).T
# y=b['target']

x=pd.DataFrame(b.data,columns=b.feature_names)
# x1=x[['age','sex','bmi','bp']]
print(x.head())

t=pd.DataFrame(b.target,columns=['target'])
print(t.head())

y=t['target']

lo=linear_model.LogisticRegression()
lo.fit(x,y)
print('迴歸係數:',lo.coef_)
print('截距:',lo.intercept_)

print('混淆矩陣')
preds=lo.predict(x)
print(pd.crosstab(b['target'], preds))

print((193+346)/(193+346+19+11))
print(lo.score(x,y))

# print((804+228)/(804+222+23+228))
# print(lo.score(x,y))


xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3,random_state=5)

lm=linear_model.LogisticRegression()
lm.fit(xtrain,ytrain)
# print('迴歸係數:',lm.coef_)
# print('截距:',lm.intercept_)

coef=pd.DataFrame(b.feature_names,columns=['features'])
coef['estimatedcofficients']=lm.coef_
print(coef)
pr=lm.predict()

pt=lm.predict(xtrain)
pte=lm.predict(xtest)
print(pt[0:5])
