import tensorflow as tf

x = tf.Variable(0, name='x')

init = tf.global_variables_initializer()

with tf.Session() as session:
  session.run(init)
  for i in range(5):
    x = x + 1
    print(session.run(x))

