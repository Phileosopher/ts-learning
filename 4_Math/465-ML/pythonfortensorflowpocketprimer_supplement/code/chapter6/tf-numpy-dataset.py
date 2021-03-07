import tensorflow as tf
import numpy as np

x = np.arange(0, 10)

# make a dataset from a numpy array
dataset = tf.data.Dataset.from_tensor_slices(x)

