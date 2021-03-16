import tensorflow as tf
import numpy as np

#def filter_fn(x):
#  return tf.reshape(tf.not_equal(x % 2, 1), [])

x = np.array([1,2,3,4,5,6,7,8,9,10])

ds = tf.data.Dataset.from_tensor_slices(x)
ds = ds.filter(lambda x: tf.reshape(tf.not_equal(x%2,1), []))
#ds = ds.filter(filter_fn)

for value in ds:
  print("value:",value)

