# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 15:26:07 2021

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
from sklearn import tree

i=datasets.load_iris()
print(i.keys())
print(i.data.shape)
print(i.feature_names)
print(i.DESCR)

x=pd.DataFrame(i.data,columns=i.feature_names)
x.columns=['speal_Length','speal_width','petal_length','petal_width']
print(x.head())

y=pd.DataFrame(i.target,columns=['target'])
print(y.head())

y=i['target']

colmap=np.array(['r','g','y'])
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.subplots_adjust(hspace=.5)
plt.scatter(x['speal_Length'], x['speal_width'], color=colmap[y])
plt.subplot(1,2,2)
plt.subplots_adjust(hspace=.5)
plt.scatter(x['petal_length'], x['petal_width'], color=colmap[y])
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3,random_state=1)
plt.show()

# dtree=tree.DecisionTreeClassifier(max_depth=3)
# dtree.fit(xtrain,ytrain)

# print('準確率:',dtree.score(xtest,ytest))
# print(dtree.predict(xtest))
# print(ytest)
