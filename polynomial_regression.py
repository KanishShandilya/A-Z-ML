#importing dataset


import numpy as np

import pandas as pd

import matplotlib.pyplot as plt


#importing dataset

df=pd.read_csv('Position_Salaries.csv')

#Creating matrix of features

X=df.iloc[:,1:2]

y=df.iloc[:,2]

#we will not divide our data as dataset is small

#Feature Scaling won't be needed


#Creating Linear Regression Model

from sklearn.linear_model import LinearRegression

reg=LinearRegression()

reg.fit(X,y)


#Importing Polynomial Features class to transform our matrix of features

from sklearn.preprocessing import PolynomialFeatures

poly= PolynomialFeatures(degree=4)

X_poly=poly.fit_transform(X)


#Creating new LinearRegression Model By X_poly

reg2=LinearRegression()

reg2.fit(X_poly,y)


#Visualising Linear Regression model result

plt.scatter(X,y,color="red")

plt.plot(X,reg.predict(X),color="red")

plt.show()


#Visulaising Polynomial Regression model result

plt.scatter(X,y,color="red")

plt.plot(X,reg2.predict(poly.fit_transform(X)),color="blue")

plt.show()


#Predicting salary using LinearRegression Model

reg.predict([[6.5]])

#Predicting results using Polynomial Regression model

reg2.predict(poly.fit_transform([[6.5]]))







