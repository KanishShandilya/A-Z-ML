#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import dataset
dataset=pd.read_csv('Mall_Customers.csv')
X=dataset.iloc[:,[3,4]].values

#Finding optimal Numbers of Clusters Using Dendrogram
import scipy.cluster.hierarchy as sch
Z=sch.linkage(X,method='ward')
dendrograms=sch.dendrogram(Z)
plt.show()

#Fitting Model to clusters
from sklearn.cluster import AgglomerativeClustering
hc=AgglomerativeClustering(n_clusters=5,affinity='euclidean',linkage='ward')
y_hc=hc.fit_predict(X)

#Visualize
plt.scatter(X[y_hc==0,0],X[y_hc==0,1],s=100,color='red')
plt.scatter(X[y_hc==1,0],X[y_hc==1,1],s=100,color='green')
plt.scatter(X[y_hc==2,0],X[y_hc==2,1],s=100,color='blue')
plt.scatter(X[y_hc==3,0],X[y_hc==3,1],s=100,color='cyan')
plt.scatter(X[y_hc==4,0],X[y_hc==4,1],s=100,color='magenta')
plt.show()