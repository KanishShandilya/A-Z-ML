#importing libraries

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt


#importing dataset

dataset=pd.read_csv("50_Startups.csv")

X=dataset.iloc[:,:-1].values

y=dataset.iloc[:,4].values


#Encoding Categorical Data

from sklearn.preprocessing import LabelEncoder,OneHotEncoder

labelencoder=LabelEncoder()

X[:,3]=labelencoder.fit_transform(X[:,3])

onehotencoder=OneHotEncoder(categorical_features=[3])

X=onehotencoder.fit_transform(X).toarray()


#Avoiding Dummy Variable Trap

X=X[:,1:]


#Spliting Test and Train Data

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)


#FeatureScaling will be taken care by Library itself


#Fitting Dataset to our model

from sklearn.linear_model import LinearRegression

regressor=LinearRegression()

regressor.fit(X_train,y_train)


#Predicting results

y_pred=regressor.predict(X_test)

#importing library for backward elimination
import statsmodels.formula.api as sm

#Adding ones column at begining of independent variable matrix 
X=np.append(arr=np.ones((50,1)).astype(int),values=X,axis=1)

#Creating optimal X from which we will remove columns
X_opt=X[:,[0,1,2,3,4,5]]#we specify each index seperatly so that we can remove it

regressor_ols=sm.OLS(endog=y,exog=X_opt).fit()
#endog->Independent Variable
#exog->Matrix of independent variable but doesn't include constant by default

#For p-values ans summary
regressor_ols.summary()

#Removing one with highest p-value
X_opt=X[:,[0,1,3,4,5]]
regressor_ols=sm.OLS(endog=y,exog=X_opt).fit()

regressor_ols.summary()

X_opt=X[:,[0,3,4,5]]
regressor_ols=sm.OLS(endog=y,exog=X_opt).fit()

regressor_ols.summary()

X_opt=X[:,[0,3,5]]
regressor_ols=sm.OLS(endog=y,exog=X_opt).fit()

regressor_ols.summary()

X_opt=X[:,[0,3]]
regressor_ols=sm.OLS(endog=y,exog=X_opt).fit()

regressor_ols.summary()

#Predicting with new values
reg=LinearRegression()
reg.fit(X_train[:,[2]],y_train)

y_p=reg.predict(X_test[:,[2]])

