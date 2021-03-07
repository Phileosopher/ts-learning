import tensorflow as tf

W = tf.Variable([.5], dtype=tf.float32)
b = tf.Variable([-1], dtype=tf.float32)
x = tf.Variable([0],  dtype=tf.float32)
linear_model = W * x + b

y = tf.Variable([0],  dtype=tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
  
print(loss, {x: [1,2,3,4], y: [0,-1,-2,-3]})

