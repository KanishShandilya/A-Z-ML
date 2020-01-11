#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing dataset
dataset=pd.read_csv('Position_Salaries.csv')
X=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2].values

#Feature Scaling won't be needed
#We will not split data

#importing regressor
from sklearn.ensemble import RandomForestRegressor
reg=RandomForestRegressor(n_estimators=300)
reg.fit(X,y)

#predicting data
reg.predict([[6.5]])

#Visualizing Data
X_grid=np.arange(min(X),max(X),0.01)
X_grid=X_grid.reshape(len(X_grid),1)
plt.scatter(X,y,color='blue')

plt.plot(X_grid,reg.predict(X_grid),color='red')