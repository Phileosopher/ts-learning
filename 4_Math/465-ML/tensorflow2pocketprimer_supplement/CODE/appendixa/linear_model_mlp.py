import tensorflow as tf
import numpy as np

# generate x data
x = np.arange(-1,1,0.2)
x = np.reshape(x, [-1,1])

# define a linear equation plus "perturbation"
y = 2 * x + 3 + np.random.uniform(-0.1, 0.1, x.shape)
#x = x         + np.random.uniform(-0.1, 0.1, x.shape)

# build 2-layer MLP network 
model = tf.keras.models.Sequential()

# 1st MLP has 8 units (perceptron), input is 1-dim
model.add(tf.keras.layers.Dense(units=8, input_dim=1))

# 2nd MLP has 1 unit, output is 1-dim
model.add(tf.keras.layers.Dense(units=1))

# print summary to double check the network
model.summary()

# create a nice image of the network model
tf.keras.utils.plot_model(model, to_file='linear-model.png', show_shapes=True)

# indicate the loss function and use sgd as optimizer
model.compile(loss='mse', optimizer='sgd')

# feed the network with complete dataset (1 epoch) 100 times
# batch size of sgd is 4
model.fit(x, y, epochs=100, batch_size=4)

# simple validation by predicting the output based on x
ypred = model.predict(x)

# linear algebra method
ones = np.ones(x.shape)

# A is the concat of x and 1s
A = np.concatenate([x,ones], axis=1)

# compute k using using pseudo-inverse
k = np.matmul(np.linalg.pinv(A), y) 
print("k (Linear Algebra Method):")
print(k)

# predict the output using linear algebra solution
yla = np.matmul(A, k)

# print ground truth, linear algebra, MLP solutions
outputs = np.concatenate([y, yla, ypred], axis=1)
print("Ground Truth, Linear Alg Prediction, MLP Prediction")
print(outputs)

# Uncomment to see the output for a new input data 
# that is not part of the training data.
# x = np.array([2])
# ypred = model.predict(x)
# print(ypred)

