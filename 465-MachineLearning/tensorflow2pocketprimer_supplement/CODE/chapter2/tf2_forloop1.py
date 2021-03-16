import tensorflow as tf # tf2-loop-eager2.py

a = tf.constant(12)

while not tf.equal(a, 1):
  if tf.equal(a % 2, 0):
    a = a / 2
  else:
    a = 3 * a + 1
  print(a)

