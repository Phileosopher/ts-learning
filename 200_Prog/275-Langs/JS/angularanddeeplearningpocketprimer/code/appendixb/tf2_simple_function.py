import tensorflow as tf

def func():
  a = tf.constant([[10,10],[11.,1.]])
  b = tf.constant([[1.,0.],[0.,1.]])
  c = tf.Variable(12.)
  d = tf.matmul(a, b) + c
  return d

print(func().numpy())

