import tensorflow as tf

A = tf.constant(3.0)
B = tf.fill([2,3], 5.0)
C = tf.constant([3.0, 4.0])

@tf.function
def show_rank(x):
  return tf.rank(x)
  
print('A:',show_rank(A))
print('B:',show_rank(B))
print('C:',show_rank(C))

