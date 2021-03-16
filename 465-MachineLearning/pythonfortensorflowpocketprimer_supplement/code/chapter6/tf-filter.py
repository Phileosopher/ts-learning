import tensorflow as tf
import numpy as np

#def filter_fn(x):
#  return tf.reshape(tf.not_equal(x % 2, 1), [])

x = np.array([1,2,3,4,5,6,7,8,9,10])

ds = tf.data.Dataset.from_tensor_slices(x)
ds = ds.filter(lambda x: tf.reshape(tf.not_equal(x%2,1), []))
#ds = ds.filter(filter_fn)

iterator = ds.make_one_shot_iterator()
next_element = iterator.get_next()

with tf.Session() as sess:
  try: 
    while True:
      value = sess.run(next_element)
      print("value:",value)
  except tf.errors.OutOfRangeError:
    pass

