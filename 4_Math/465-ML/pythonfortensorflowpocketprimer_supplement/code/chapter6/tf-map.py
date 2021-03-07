import tensorflow as tf
import numpy as np

# a simple Numpy array
x = np.array([[1],[2],[3],[4]])

# make a dataset from a numpy array
dataset = tf.data.Dataset.from_tensor_slices(x)

# a lambda expression to double each value
dataset = dataset.map(lambda x: x*2)

# define an iterator 
iter = dataset.make_one_shot_iterator()
el = iter.get_next()

with tf.Session() as sess:
  for _ in range(len(x)):
    print("value:",sess.run(el))

