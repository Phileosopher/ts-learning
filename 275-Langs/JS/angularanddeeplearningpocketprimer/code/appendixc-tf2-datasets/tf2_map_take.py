import tensorflow as tf
import numpy as np

x = np.array([[1],[2],[3],[4]])

# make a ds from a numpy array
ds = tf.data.Dataset.from_tensor_slices(x)
ds = ds.map(lambda x: x*2).map(lambda x: x+1).map(lambda x: x**3)

for value in ds.take(4):
  print("value:",value)

