import tensorflow as tf
import numpy as np

ds = tf.data.Dataset.from_tensor_slices([1,2,3,4,5])
ds = ds.filter(lambda x: x < 4) # [1,2,3]

print("First iteration:")
for value in ds:
  print("value:",value)

# "tf.math.equal(x, y)" is required for equality comparison
def filter_fn(x):
  return tf.math.equal(x, 1)

ds = ds.filter(filter_fn) 

print("Second iteration:")
for value in ds:
  print("value:",value)

