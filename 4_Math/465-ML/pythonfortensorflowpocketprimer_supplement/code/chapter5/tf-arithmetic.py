import tensorflow as tf 

a = tf.add(4, 2)
b = tf.subtract(8, 6)
c = tf.multiply(a, 3)
d = tf.div(a, 6)

with tf.Session() as sess:
  print(sess.run(a)) # 6
  print(sess.run(b)) # 2
  print(sess.run(c)) # 18
  print(sess.run(d)) # 1

