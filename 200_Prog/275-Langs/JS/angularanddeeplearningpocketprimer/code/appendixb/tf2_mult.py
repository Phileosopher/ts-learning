import tensorflow as tf

m1 = tf.constant([[3., 3.]])  # 1x2
m2 = tf.constant([[2.],[2.]]) # 2x1
p1 = tf.matmul(m1, m2)        # 1x1

@tf.function
def compute_values():
  print('m1:',m1)
  print('m2:',m2)
  print('p1:',p1)

compute_values()

