import tensorflow as tf
import itertools

# RuntimeError: dataset.make_initializable_iterator 
# is not supported when eager execution is enabled.
# tf.enable_eager_execution()

dataset = tf.data.TextLineDataset("file.txt")
dataset = dataset.map(lambda string: tf.string_split([string]).values)

#iterator = dataset.make_initializable_iterator()
#next_element = iterator.get_next()
#init_op = iterator.initializer

iterator = dataset.make_one_shot_iterator()
next_element = iterator.get_next()
with tf.Session() as sess:
  print(sess.run(next_element))
  print(sess.run(next_element))
  print(sess.run(next_element))

