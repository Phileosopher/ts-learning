import tensorflow as tf
import numpy as np

x1 = np.array([1,2,3,4,5])
x2 = np.array([6,7,8,9,10])

ds1 = tf.data.Dataset.from_tensor_slices(x1)
ds2 = tf.data.Dataset.from_tensor_slices(x2)
ds3 = ds1.concatenate(ds2)

try: 
 #for value in ds3.take(20):
  for value in ds3:
    print("value:",value)
except tf.errors.OutOfRangeError:
  pass

