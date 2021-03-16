import tensorflow as tf
import numpy as np

ds1 = tf.data.Dataset.range(100)
ds2 = tf.data.Dataset.range(0, -100, -1)
ds3 = tf.data.Dataset.zip((ds1, ds2))
ds4 = ds3.batch(4)

iterator = ds4.make_one_shot_iterator()
next_element = iterator.get_next()

with tf.Session() as sess:
  print(sess.run(next_element))  
  print(sess.run(next_element))  
  print(sess.run(next_element))  

# output:
# ([0, 1, 2,   3],   [ 0, -1,  -2,  -3])
# ([4, 5, 6,   7],   [-4, -5,  -6,  -7])
# ([8, 9, 10, 11],   [-8, -9, -10, -11])

