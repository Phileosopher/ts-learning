import tensorflow as tf
import numpy as np

W = tf.Variable([.5], dtype=tf.float32)
b = tf.Variable([-1], dtype=tf.float32)
x = tf.Variable([0],  dtype=tf.float32)
lm = W * x + b

y = tf.Variable([0],  dtype=tf.float32)
squared_deltas = tf.square(lm - y)
loss = tf.reduce_sum(squared_deltas)
  
x = np.array([1,2,3,4]) 
y = np.array([0,-1,-2,-3])

@tf.function
def compute_values(xi, yi):
  yhat = W*xi + b 
  return (yhat-yi)

#for i in len(x):
for i in range(4):
  loss = compute_values(x[i], y[i])
  print("loss:", loss)

