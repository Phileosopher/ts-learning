import tensorflow as tf
import itertools

dataset = tf.data.TextLineDataset("file.txt")
dataset = dataset.map(lambda string: tf.string_split([string]).values)
iterator = dataset.make_initializable_iterator()
next_element = iterator.get_next()
init_op = iterator.initializer

with tf.Session() as sess:
  # Initialize the iterator
  sess.run(init_op)
  print(sess.run(next_element))
  print(sess.run(next_element))
  print(sess.run(next_element))
  # Reset the iterator at the beginning
  sess.run(init_op)
  print(sess.run(next_element))

