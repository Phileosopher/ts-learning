import tensorflow as tf
import numpy as np

x = np.random.sample((100,2))

ds = tf.data.Dataset.from_tensor_slices(x)
iter = tf.compat.v1.data.make_one_shot_iterator(ds)
el = iter.get_next()

print(iter.get_next())

