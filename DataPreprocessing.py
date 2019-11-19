#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing datasets
df=pd.read_csv('Data.csv')
X=df.iloc[:,:-1].values
Y=df.iloc[:,3].values

#handling missing data
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN',strategy="mean",axis=0)
X[:,1:3]=imputer.fit_transform(X[:,1:3])

#handling categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencode=LabelEncoder()
Y=labelencode.fit_transform(Y)
labelencoder=LabelEncoder()
X[:,0]=labelencoder.fit_transform(X[:,0])
onehotencoder=OneHotEncoder(categorical_features=[0])
X=onehotencoder.fit_transform(X).toarray()
#spliting training and testing data
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)
#Feature Scaling
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
X_train=ss.fit_transform(X_train)
X_test=ss.transform(X_test)