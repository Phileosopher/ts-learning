import tensorflow as tf
import numpy as np

# two Numpy arrays with random numbers
features, labels = (np.random.sample((100,2)), np.random.sample((100,1)))
dataset = tf.data.Dataset.from_tensor_slices((features,labels))

iter = dataset.make_one_shot_iterator()
el = iter.get_next()

with tf.Session() as sess:
  print(sess.run(el))

