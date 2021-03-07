import tensorflow as tf

try:
  tf.constant(1) + tf.constant(1.0)
except tf.errors.InvalidArgumentError as ex:
  print(ex)

try:
  tf.constant(1.0, dtype=tf.float64) + tf.constant(1.0)
except tf.errors.InvalidArgumentError as ex:
  print(ex)

