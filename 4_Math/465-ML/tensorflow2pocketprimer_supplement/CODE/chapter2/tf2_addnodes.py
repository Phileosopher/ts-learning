import tensorflow as tf

a1 = tf.Variable(7,  tf.float32)
a2 = tf.Variable(13, tf.float32)
a3 = a1 + a2

@tf.function
def compute_values(a1, a2):
  return a1 + a2

result = compute_values(a1, a2)
print("a1 + a2 =",result)

