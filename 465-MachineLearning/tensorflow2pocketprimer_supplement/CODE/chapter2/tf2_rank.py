import tensorflow as tf

b1 = tf.constant(7)
b2 = tf.constant([3,7])
b3 = tf.constant([[3,7],[11,13]])

print("rank b1:",tf.rank(b1))
print("rank b2:",tf.rank(b2))
print("rank b3:",tf.rank(b3))

# rank b1: tf.Tensor(0, shape=(), dtype=int32)
# rank b2: tf.Tensor(1, shape=(), dtype=int32)
# rank b3: tf.Tensor(2, shape=(), dtype=int32)

