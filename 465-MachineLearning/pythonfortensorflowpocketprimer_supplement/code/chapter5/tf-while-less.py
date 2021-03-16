import tensorflow as tf

x = tf.Variable(0., name='x')
threshold = tf.constant(5.)

model = tf.global_variables_initializer()

with tf.Session() as session:
  session.run(model)
  while session.run(tf.less(x, threshold)):
    x = x + 1
    x_value = session.run(x)
    print(x_value)

