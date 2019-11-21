#Simple Linear Regression

# Importing the libraries

import numpy as np

import matplotlib.pyplot as plt

import pandas as pd


# Importing the dataset

dataset = pd.read_csv('Salary_Data.csv')

X = dataset.iloc[:, :-1].values

y = dataset.iloc[:, 1].values


# Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)


# Feature Scaling is done in Simple Regression itself

#Fitting data into Simple regression Model
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)
#predicting values
y_pred=regressor.predict(X_test)

#visualizing predicted results
plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color="blue")
plt.title("Salary Vs Experience")
plt.xlabel("Experience(in yrs)")
plt.ylabel("Salary")
#visualizing test results
plt.scatter(X_test,y_test,color='red')
plt.plot(X_train,regressor.predict(X_train),color="blue")
plt.title("Salary Vs Experience")
plt.xlabel("Experience(in yrs)")
plt.ylabel("Salary")
