import tensorflow as tf
import numpy as np

x1 = tf.data.Dataset.range(8).reduce(np.int64(0), lambda x, _: x + 1) # 8
x2 = tf.data.Dataset.range(8).reduce(np.int64(0), lambda x, y: x + y) # 28
print("x1:",x1)
print("x2:",x2)

