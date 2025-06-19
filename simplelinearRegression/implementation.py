import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('simplelinearRegression/height-weight.csv')
plt.scatter(df['Weight'],df['Height'])
plt.xlabel("Weight")
plt.ylabel("Height")
x=df[['Weight']]
y=df['Height']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=42)
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)
from sklearn.linear_model import LinearRegression
regression=LinearRegression(n_jobs=-1)
regression.fit(x_train,y_train)
print("Coefficient or slope:",regression.coef_)
print("Intercept:",regression.intercept_)
#plt.scatter(x_train,y_train)
#plt.plot(x_train,regression.predict(x_train))
#plt.show()
print(regression.predict(x_test))
y_pred=regression.predict(x_test)
from sklearn.metrics import mean_absolute_error,mean_squared_error
mse=mean_squared_error(y_test,y_pred)
mae=mean_absolute_error(y_test,y_pred)
rmse=np.sqrt(mse)
print(mse)
print(mae)
print(rmse)
from sklearn.metrics import r2_score
score=r2_score(y_test,y_pred)
print(score)
