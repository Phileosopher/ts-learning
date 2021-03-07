import tensorflow as tf
import numpy as np

x = np.random.sample((100,2))

# make a dataset from a numpy array
dataset = tf.data.Dataset.from_tensor_slices(x)

iter = dataset.make_one_shot_iterator()
el = iter.get_next()

with tf.Session() as sess:
  print(sess.run(el))

