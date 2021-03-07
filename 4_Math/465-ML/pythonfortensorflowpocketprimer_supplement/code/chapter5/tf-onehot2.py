import tensorflow as tf

# Generate one-hot array using idx
idx = tf.get_variable("idx", initializer=tf.constant([2, 0, -1, 0]))

target = tf.one_hot(idx, 3, 2, 0)

init = tf.global_variables_initializer()

with tf.Session() as sess:
  sess.run(init)
  print(sess.run(target))

