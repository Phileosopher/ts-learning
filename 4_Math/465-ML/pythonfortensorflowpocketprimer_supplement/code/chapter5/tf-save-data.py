import tensorflow as tf

x = tf.constant(5,name="x")
y = tf.constant(8,name="y")
z = tf.Variable(2*x+3*y, name="z")
init = tf.global_variables_initializer()

with tf.Session() as session:
  writer = tf.summary.FileWriter("./tf_logs",session.graph)
  session.run(init)
  print('z = ',session.run(z)) # =>  z = 34

# launch tensorboard: tensorboard –logdir=./tf_logs

