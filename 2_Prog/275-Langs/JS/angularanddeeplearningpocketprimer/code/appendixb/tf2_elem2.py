import tensorflow as tf

arr2 = tf.constant([[1,2],[2,3]])

#@tf.function # DO NOT USE THIS DECORATOR
def compute_values():
  print('arr2: ',arr2)
  print('[0]:  ',arr2[0])
  print('[1]:  ',arr2[1])

compute_values()

