import tensorflow as tf
import tensorflow.contrib.eager as tfe

tfe.enable_eager_execution()

#x = tf.Variable(0, name='x')
x = tf.contrib.eager.Variable(0, name='x')

for i in range(5):
  print(x)
  x = x + 1

