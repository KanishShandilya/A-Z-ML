#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

#importing dataset
dataset=pd.read_csv('Churn_Modelling.csv')
X=dataset.iloc[:,3:13].values
y=dataset.iloc[:,13].values

#Label Encoder
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelEncoder_X_1=LabelEncoder()
X[:,1]=labelEncoder_X_1.fit_transform(X[:,1])

labelEncoder_X_2=LabelEncoder()
X[:,2]=labelEncoder_X_2.fit_transform(X[:,2])

ohe=OneHotEncoder(categorical_features=[1])
X=ohe.fit_transform(X).toarray()
X=X[:,1:]


#Spliting to train test data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

#Scaling Data
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
X_train=sc_x.fit_transform(X_train)
X_test=sc_x.fit_transform(X_test)


#making ann
model=tf.keras.Sequential()
model.add(tf.keras.layers.Dense(6,activation='relu',input_dim=11))
model.add(tf.keras.layers.Dense(6,activation='relu'))
model.add(tf.keras.layers.Dense(1,activation='sigmoid'))


model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])


model.fit(X_train,y_train,batch_size=10,epochs=100)



y_pred=model.predict(X_test) > 0.5

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)