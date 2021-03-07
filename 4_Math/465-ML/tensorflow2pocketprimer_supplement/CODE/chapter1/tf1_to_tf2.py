import tensorflow as tf 

import tensorflow as tf
a = tf.constant([[10,10],[11.,1.]])
b = tf.constant([[1.,0.],[0.,1.]])
c = tf.Variable(12.)
d = tf.matmul(a, b) 
e = tf.matmul(a, b) + c

print("d:",d.numpy())
print("e:",e.numpy())

