import tensorflow as tf

ds1 = tf.data.Dataset.from_tensor_slices(tf.range(8))
ds1 = ds1.take(5)

iterator = ds1.make_one_shot_iterator()
next_element = iterator.get_next()

with tf.Session() as sess:
  try: 
    while True:
      value = sess.run(next_element)
      print("value:",value)
  except tf.errors.OutOfRangeError:
    pass

