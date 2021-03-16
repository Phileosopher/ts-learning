#!pip install tf-nightly-2.0-preview 
import tensorflow as tf
import numpy as np

print("tf.version:",tf.__version__)
# only works with TF 1.13

x = np.arange(0, 33)
dx = tf.data.Dataset.from_tensor_slices(x).batch(3)
iterator = dx.make_initializable_iterator()

with tf.Session() as sess:
  sess.run(iterator.initializer)
  for i in range(5):
    next_element = iterator.get_next()
    val = sess.run(next_element)
    print(val)
    if i % 9 == 0 and i > 0:
      sess.run(iterator.initializer)

