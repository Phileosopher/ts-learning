import tensorflow as tf

a  = tf.exp(1.0)
b  = tf.exp(-2.0)
s1 = tf.sigmoid(2.0)
s2 = 1.0/(1.0 + b)
t2 = tf.tanh(2.0)

with tf.Session() as sess:
  print('a: ', sess.run(a))
  print('b: ', sess.run(b))
  print(’s1:', sess.run(s1))
  print('s2:', sess.run(s2))
  print('t2:', sess.run(t2))

