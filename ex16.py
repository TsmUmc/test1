# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 11:53:45 2021

@author: Administrator
"""

import pandas as pd
import numpy as np
from sklearn import cluster
import matplotlib.pyplot as plt
from sklearn import datasets
import sklearn.metrics as sm
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

i= datasets.load_iris()
x2=i.data
x2=x2[:,2:4]

# x=np.array([[1,2],[2,2],[2,3],[8,7],[8,8],[87,870]])
cl=DBSCAN(eps=0.3,min_samples=10) 
cl.fit(x2)
yp=cl.labels_ 
     
# co=np.array(['r','g','y'])
# plt.figure(figsize=(10,5))
# plt.subplot(121)
# plt.scatter(x['petal_Length'],x['petal_width'], c=co[k2.labels_])
# plt.show()

# df=pd.DataFrame({'L':[51,50,40,43,30,32],'w':[10,9,7,6,3,4]})
# k=3
# w=datasets.load_wine()

# x=pd.DataFrame(w.data,columns=w.feature_names)
# x.columns=['sepal_Length','sepal_width','petal_Length','petal_width']

y=w.target
k=3

k2=cluster.KMeans(n_clusters=k,random_state=12)
k2.fit(x)
print(k2.labels_)
print(y)

y2=np.choose(k2.labels_,[2,0,1]).astype(np.int64)
print(y2)

print(sm.accuracy_score(y,y2))
print(sm.confusion_matrix(y,y2))


co=np.array(['r','g','y'])
plt.figure(figsize=(10,5))
plt.subplot(121)
plt.scatter(x['petal_Length'],x['petal_width'], c=co[k2.labels_])
plt.show()

# k2=cluster.KMeans(n_clusters=k,random_state=12)
