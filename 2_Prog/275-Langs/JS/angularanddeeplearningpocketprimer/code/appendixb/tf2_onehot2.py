import tensorflow as tf

idx = tf.constant([2, 0, -1, 0])
target = tf.one_hot(idx, 3, 2, 0)

@tf.function
def compute_values():
  print(idx) 
  print(target) 

compute_values()

