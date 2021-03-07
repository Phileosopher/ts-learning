import tensorflow as tf
import numpy as np

print("tf.version:",tf.__version__)
# only works with TF 1.13

ds = tf.data.Dataset.range(100)
ds = ds.map(lambda x: tf.fill([tf.cast(x, tf.int32)], x))
ds = ds.padded_batch(4, padded_shapes=(None,))

iterator = ds.make_one_shot_iterator()
next_element = iterator.get_next()

with tf.Session() as sess:
  print(sess.run(next_element))  
  print(sess.run(next_element))  

# first print statement: 
# [[0, 0, 0], [1, 0, 0], [2, 2, 0], [3, 3, 3]]
# second print statement:
# [[4, 4, 4, 4, 0, 0, 0],
# [5, 5, 5, 5, 5, 0, 0],
# [6, 6, 6, 6, 6, 6, 0],
# [7, 7, 7, 7, 7, 7, 7]]

