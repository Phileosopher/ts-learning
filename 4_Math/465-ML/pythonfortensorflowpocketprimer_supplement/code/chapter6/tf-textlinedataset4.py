import tensorflow as tf
import itertools

dataset = tf.data.TextLineDataset("file.txt")
dataset = dataset.map(lambda string: tf.string_split([string]).values)
dataset = dataset.shuffle(buffer_size=3)

iterator = dataset.make_one_shot_iterator()
next_element = iterator.get_next()

with tf.Session() as sess:
  for i in range(5):
    print(sess.run(next_element))

