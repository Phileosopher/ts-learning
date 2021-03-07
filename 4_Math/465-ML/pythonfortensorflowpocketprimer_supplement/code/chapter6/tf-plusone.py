import tensorflow as tf
import numpy as np

x = np.arange(0, 10)

# create dataset object from numpy array
dx = tf.data.Dataset.from_tensor_slices(x)

dx.map(lambda x: x + 1)

# create a one-shot iterator
iterator = dx.make_one_shot_iterator()

# extract an element
next_element = iterator.get_next()

with tf.Session() as sess:
  for i in range(10):
    val = sess.run(next_element)
    print("val:",val)

