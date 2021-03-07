import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler

iris = load_iris()
X = iris['data']
y = iris['target']

#print("iris data:",X)
#print("iris target:",y)

# scale the X values so they are between 0 and 1
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size = 0.2)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(activation='relu', input_dim=4, units=4, 
                     kernel_initializer='uniform'))

model.add(tf.keras.layers.Dense(activation='relu', units=4, 
                     kernel_initializer='uniform'))

model.add(tf.keras.layers.Dense(activation='sigmoid', units=1, 
                     kernel_initializer='uniform'))
#model.add(tf.keras.layers.Dense(1, activation='softmax'))

model.compile(optimizer='adam',loss='mean_squared_error',metrics=['accuracy'])

model.fit(X_train, y_train, batch_size=10, epochs=100)

# Predicting the Test set results
y_pred = model.predict(X_test)

# scatter plot of test values-vs-predictions
fig, ax = plt.subplots()
ax.scatter(y_test, y_pred)
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r*--')
ax.set_xlabel('Calculated')
ax.set_ylabel('Predictions')
plt.show()

