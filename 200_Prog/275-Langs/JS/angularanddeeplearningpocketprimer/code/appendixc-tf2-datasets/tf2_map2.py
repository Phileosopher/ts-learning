import tensorflow as tf
import numpy as np

# a simple Numpy array
x = np.array([[1],[2],[3],[4]])

# make a dataset from a numpy array
ds = tf.data.Dataset.from_tensor_slices(x)

# METHOD #1: THE LONG WAY
# a lambda expression to double each value
#ds = ds.map(lambda x: x*2)
# a lambda expression to add one to each value
#ds = ds.map(lambda x: x+1)
# a lambda expression to cube each value
#ds = ds.map(lambda x: x**3)

# METHOD #2: A SHORTER WAY
ds = ds.map(lambda x: x*2).map(lambda x: x+1).map(lambda x: x**3)

for value in ds:
  print("value:",value)

