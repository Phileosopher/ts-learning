import tensorflow as tf

ds = tf.data.Dataset.from_tensor_slices(tf.range(8))
ds = ds.take(5)

for value in ds.take(20):
  print("value:",value)

