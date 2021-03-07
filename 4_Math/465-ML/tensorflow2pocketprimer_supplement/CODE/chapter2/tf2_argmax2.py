import tensorflow as tf
import numpy as np

# initialize array of arrays:
a = [[1,2,3], [30,20,10], [40,60,50]]
b = tf.Variable(a, name='b')

print("index of max values in b: ",tf.argmax(input=b,axis=1))

#index of max values in b:  tf.Tensor([2 0 1], shape=(3,), dtype=int64)

