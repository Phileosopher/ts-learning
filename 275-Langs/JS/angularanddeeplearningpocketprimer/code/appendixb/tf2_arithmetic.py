import tensorflow as tf 

#@tf.function # DO NOT USE THIS DECORATOR 
def compute_values():
  a = tf.add(4, 2)
  b = tf.subtract(8, 6)
  c = tf.multiply(a, 3)
  d = tf.math.divide(a, 6)

  print(a) # 6
  print(b) # 2
  print(c) # 18
  print(d) # 1

compute_values()

