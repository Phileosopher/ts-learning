import tensorflow as tf
import numpy as np

x = np.arange(0, 34)

# make a ds from a numpy array
ds = tf.data.Dataset.from_tensor_slices(x).batch(3)

for value in ds:
  print("value:",value)

