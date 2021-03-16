import tensorflow as tf 

x = tf.placeholder("float", [None, 3])
y = x * 2
z = x ** 3

with tf.Session() as session:
  x_data = [[1, 2, 3],
            [4, 5, 6],]

  result1 = session.run(y, feed_dict={x: x_data})
  print('y:',result1.eval())

  result2 = session.run(z, feed_dict={x: x_data})
  print('z:',result2.eval())

