import tensorflow as tf
import numpy as np

print("tf.version:",tf.__version__)
# only works with TF 1.13

x = np.arange(0, 33)
dx = tf.data.Dataset.from_tensor_slices(x).batch(3)
iterator = dx.make_one_shot_iterator()
next_element = iterator.get_next()

with tf.Session() as sess:
  for i in range(11):
    val = sess.run(next_element)
    print(val)

