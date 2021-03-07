import tensorflow as tf
import numpy as np

elems = np.array([1, 2, 3, 4, 5])
doubles = tf.map_fn(lambda x: 2 * x, elems)
print("doubles:",doubles)
# [2, 4, 6, 8, 10]

squares = tf.map_fn(lambda x: x * x, elems)
print("squares:",squares)
# [1, 4, 9, 16, 25]

elems = (np.array([1, 2, 3]), np.array([-1, 1, -1]))
neg_pos = tf.map_fn(lambda x: x[0] * x[1], elems, dtype=tf.int64)
print("neg_pos:",neg_pos)
# [-1, 2, -3]

elems = np.array([1, 2, 3])
pos_neg = tf.map_fn(lambda x: (x, -x), elems, dtype=(tf.int64, tf.int64))
print("pos_neg:",pos_neg)
# pos_neg[0]: [1, 2, 3]
# pos_neg[1]: [-1, -2, -3]

