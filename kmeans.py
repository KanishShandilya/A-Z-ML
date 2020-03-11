#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing dataset
dataset=pd.read_csv('Mall_Customers.csv')
X=dataset.iloc[:,[3,4]].values

#Finding Optimal Numbers of clusters using Elbow Method
from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',n_init=10,max_iter=300)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,11),wcss)

#Making model with optimal no. clusters
kmeans=KMeans(n_clusters=5,init='k-means++',n_init=10,max_iter=300)
y_kmeans=kmeans.fit_predict(X)

#Visualizing Results

plt.scatter(X[y_kmeans==0,0],X[y_kmeans==0,1],s=50,c='red',label='C1')
plt.scatter(X[y_kmeans==1,0],X[y_kmeans==1,1],s=50,c='green',label='C2')
plt.scatter(X[y_kmeans==2,0],X[y_kmeans==2,1],s=50,c='blue',label='C3')
plt.scatter(X[y_kmeans==3,0],X[y_kmeans==3,1],s=50,c='cyan',label='C4')
plt.scatter(X[y_kmeans==4,0],X[y_kmeans==4,1],s=50,c='magenta',label='C5')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=150,c='yellow',label='centroids')

plt.show()

