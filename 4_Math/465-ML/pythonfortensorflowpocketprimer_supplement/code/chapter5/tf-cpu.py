import tensorflow as tf

with tf.Session() as sess: 
  m1 = tf.constant([[3., 3.]])  # 1x2
  m2 = tf.constant([[2.],[2.]]) # 2x1
  p1 = tf.matmul(m1, m2)        # 1x1
  print('m1:',sess.run(m1))
  print('m2:',sess.run(m2))
  print('p1:',sess.run(p1))

