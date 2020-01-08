#importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#importing dataset
dataset=pd.read_csv('Position_Salaries.csv')
dataset=dataset.iloc[:,1:]
#Getting Matrix of features and dependent variable
X=dataset.iloc[:,0:1].values
y=dataset.iloc[:,1].values

#Fitting data in Decision Tree Model
from sklearn.tree import DecisionTreeRegressor
reg=DecisionTreeRegressor()
reg.fit(X,y)
#Predicting values
y_pred=reg.predict([[6.5]])

#Visualizing Data
plt.scatter(X,y,color='red')
plt.plot(X,reg.predict(X),color='blue')
plt.show()
'''There is a problem with above visualization when we 
visualize data using it we're only visualizing 10 levels 1 to 10
and we're joining line b/w them what we have to do is to take each 
inteval split and then plot it so we will take a high resolution graph'''
X_grid=np.arange(min(X),max(X),0.01)
X_grid=X_grid.reshape((len(X_grid),1))
plt.scatter(X,y,color='blue')
plt.plot(X_grid,reg.predict(X_grid),color='red')
plt.show()