import tensorflow as tf
import numpy as np

# two Numpy arrays with random numbers
features, labels = (np.random.sample((100,2)), np.random.sample((100,1)))
ds = tf.data.Dataset.from_tensor_slices((features,labels))

iter = tf.compat.v1.data.make_one_shot_iterator(ds)
print(iter.get_next())

