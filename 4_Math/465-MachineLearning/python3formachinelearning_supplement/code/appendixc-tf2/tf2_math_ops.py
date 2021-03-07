import tensorflow as tf 

PI = 3.141592

#@tf.function  DO NOT USE THIS DECORATOR 
def math_values():
  print(tf.math.divide(12,8))
  print(tf.math.floordiv(20.0,8.0))
  print(tf.sin(PI))
  print(tf.cos(PI))
  print(tf.math.divide(tf.sin(PI/4.), tf.cos(PI/4.)))

math_values()
