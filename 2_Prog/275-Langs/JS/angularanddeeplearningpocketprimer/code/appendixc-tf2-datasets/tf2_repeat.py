import tensorflow as tf

ds = tf.data.Dataset.from_tensor_slices(tf.range(4))
ds = ds.repeat(2)

for value in ds.take(20):
  print("value:",value)

