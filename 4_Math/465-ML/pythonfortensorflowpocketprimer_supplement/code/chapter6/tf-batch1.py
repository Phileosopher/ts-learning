import tensorflow as tf
import numpy as np

x = np.arange(0, 33)
dx = tf.data.Dataset.from_tensor_slices(x).batch(3)
iterator = dx.make_initializable_iterator()

with tf.Session() as sess:
  sess.run(iterator.initializer)
  for i in range(15):
    next_element = iterator.get_next()
    val = sess.run(next_element)
    print(val)
    if (i + 1) % (10 // 3) == 0 and i > 0:
      sess.run(iterator.initializer)

