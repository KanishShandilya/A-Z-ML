#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing dataset
dataset=pd.read_csv('Wine.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

#Spliting dataset
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

#Standard Scaler
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

#PCA
from sklearn.decomposition import PCA
pca=PCA(n_components=3)
X_train=pca.fit_transform(X_train)
X_test=pca.transform(X_test)

#Fitting data to model
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(X_train,y_train)

#Predicting Values
y_pred=classifier.predict(X_test)

#Builging cm
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)