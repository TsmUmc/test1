# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 11:37:15 2021

@author: Administrator
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split

boston=datasets.load_boston()
# d=datasets.load_diabetes()

# iris=datasets.load_iris()
# di=datasets.load_digits()

# print(boston.keys())
# print(d.keys())
# print(iris.keys())
# print(di.keys())

# print(boston.DESCR)


# t=np.array([[67,160],[68,165],[70,167],[65,170],[80,165]])
# d=np.array([50,60,65,65,70])
x=pd.DataFrame(boston.data,columns=boston.feature_names)
print(x.head())

target=pd.DataFrame(boston.target,columns=['MEDV'])
print(target.head())

y=target['MEDV']

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3,random_state=5)

lm=LinearRegression ()
lm.fit(xtrain,ytrain)
# print('迴歸係數:',lm.coef_)
# print('截距:',lm.intercept_)

coef=pd.DataFrame(boston.feature_names,columns=['features'])
coef['estimatedcofficients']=lm.coef_
print(coef)
pr=lm.predict()

pt=lm.predict(xtrain)
pte=lm.predict(xtest)
print(pt[0:5])

MSE=np.mean((y-pt)**2)
print('mse:',MSE)
print('r^2:',lm.score(x,y))





# plt.scatter(ytest,pt)
# plt.show()
# nt=pd.DataFrame(np.array([[66,164],[86,172]]),columns=['w3','h2'])
# ps=lm.predict(nt)
# print(ps)

# plt.scatter(t,d)
# rs=lm.predict(x)
# plt.plot(t,rs,color='blue')
# plt.plot(nt,ps,color='red',marker='o',markersize=10)
# plt.show()
