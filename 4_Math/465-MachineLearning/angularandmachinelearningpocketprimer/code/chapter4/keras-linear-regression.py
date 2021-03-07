import tensorflow as tf
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

##############################################################
# Important notes for better accuracy:
1) Always standardize both input features and target variable: 
doing so only on input feature produces incorrect predictions
2) Data might not be normally distributed: check the data and 
based on the distribution apply StandardScaler, MinMaxScaler, 
Normalizer or RobustScaler
##############################################################

dataset = pd.read_csv('housing.csv')
dataset.head(2)

X = dataset.iloc[:,0:13]
y = dataset.iloc[:,13].values

from sklearn.preprocessing import  MinMaxScaler
sc = MinMaxScaler()
X  = sc.fit_transform(X)
y  = y.reshape(-1,1)
y  = sc.fit_transform(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

def build_regressor():
  regressor = tf.keras.models.Sequential()
  regressor.add(tf.keras.layers.Dense(units=13, input_dim=13))
  regressor.add(tf.keras.layers.Dense(units=1))
  regressor.compile(optimizer='adam',loss='mean_squared_error',metrics=['mae','accuracy'])
  return regressor

regressor = tf.keras.wrappers.scikit_learn.KerasRegressor(build_fn=build_regressor, batch_size=32,epochs=100)

# train and then predict:
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

fig, ax = plt.subplots()
ax.scatter(y_test, y_pred)
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()

