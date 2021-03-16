import tensorflow as tf

# constant:
aconst = tf.constant(3.0)
print(aconst)

# 2x3 constant matrix
B = tf.fill([2,3], 5.0)

with tf.Session() as sess:
  print('aconst:',sess.run(tf.rank(aconst)))
  print('rank B:',sess.run(tf.rank(B)))

