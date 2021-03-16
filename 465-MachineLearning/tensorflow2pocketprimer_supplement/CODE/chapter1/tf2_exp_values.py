import tensorflow as tf

a  = tf.exp(1.0)
b  = tf.exp(-2.0)
s1 = tf.sigmoid(2.0)
s2 = 1.0/(1.0 + b)
t2 = tf.tanh(2.0)

@tf.function # this decorator is okay
def math_values():
  print('a: ', a)
  print('b: ', b)
  print('s1:', s1)
  print('s2:', s2)
  print('t2:', t2)

math_values()

