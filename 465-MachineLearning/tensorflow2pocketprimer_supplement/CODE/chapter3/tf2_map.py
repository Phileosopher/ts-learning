import tensorflow as tf
import numpy as np

# a simple Numpy array
x = np.array([[1],[2],[3],[4]])

# make a ds from a numpy array
ds = tf.data.Dataset.from_tensor_slices(x)

# a lambda expression to double each value
ds = ds.map(lambda x: x*2)

for value in ds:
  print("value:",value)

