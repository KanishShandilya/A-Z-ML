#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing dataset
dataset=pd.read_csv('Position_Salaries.csv')
X=dataset.iloc[:,1:-1].values
y=dataset.iloc[:,-1].values

#Feature Scaling
y=y.reshape((len(y),1))
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
X=sc_x.fit_transform(X)
sc_y=StandardScaler()
y=sc_y.fit_transform(y)

#Training Model
from sklearn.svm import SVR
regressor=SVR(kernel='rbf')
regressor.fit(X,y)

#Making Predictions
y_pred=sc_y.inverse_transform(regressor.predict(sc_x.transform([[6.5]])))

#Visualizing results
plt.scatter(sc_x.inverse_transform(X),sc_y.inverse_transform(y),color='red')
plt.plot(sc_x.inverse_transform(X),sc_y.inverse_transform(regressor.predict(X)),color='blue')
plt.show()