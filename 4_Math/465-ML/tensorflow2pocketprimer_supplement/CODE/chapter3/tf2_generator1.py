import tensorflow as tf
import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10])

ds = tf.data.Dataset.from_tensor_slices(x)
ds = ds.filter(lambda x: tf.reshape(tf.not_equal(x%2,1), []))

size = 2*len(x)

try: 
  for value in ds.take(size):
    print("value:",value)
except tf.errors.OutOfRangeError:
  pass

