##########################################
# TensorFlow APIs IN THIS EXAMPLE:
# tf.nn.sigmoid(tf.matmul(...))
##########################################

import tensorflow as tf
import numpy as np

import matplotlib.pyplot as plt
trainsamples = 200
testsamples = 60

# the model, a simple input, a hidden layer (sigmoid activation)
def model(X, hidden_weights1, hidden_bias1, ow):
  hidden_layer =  tf.nn.sigmoid(tf.matmul(X, hidden_weights1)+ b)
  return tf.matmul(hidden_layer, ow)

dsX = np.linspace(-1, 1, trainsamples + testsamples).transpose()
dsY = 0.4*pow(dsX,2)+2*dsX+np.random.randn(*dsX.shape)*0.22+0.8

plt.figure() 
plt.title('Original data')
plt.scatter(dsX,dsY)
plt.show()

