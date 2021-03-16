import tensorflow as tf

W = tf.Variable([.5], dtype=tf.float32)
b = tf.Variable([-1], dtype=tf.float32)
x = tf.Variable([0],  dtype=tf.float32)
#x = tf.placeholder(tf.float32)
linear_model = W * x + b

print(linear_model, {x: [1, 2, 3, 4]})

