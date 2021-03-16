import tensorflow as tf

W = tf.Variable([.5], dtype=tf.float32)
b = tf.Variable([-1], dtype=tf.float32)
x = tf.Variable([0],  dtype=tf.float32)

@tf.function
def compute_values(x):
  lm = W*x + b
  return lm

for x in range(4):
  val = compute_values(x+1)
  print("val:", val)

