import tensorflow as tf

a1 = tf.range(3, 18, 3)
a2 = tf.range(0, 8, 2)
a3 = tf.range(-6, 6, 3)
a4 = tf.range(-10, 10, 4)

print('a1:',a1)
print('a2:',a2)
print('a3:',a3)
print('a4:',a4)

# a1: tf.Tensor([ 3  6  9 12 15], shape=(5,), dtype=int32)
# a2: tf.Tensor([0 2 4 6], shape=(4,), dtype=int32)
# a3: tf.Tensor([-6 -3  0  3], shape=(4,), dtype=int32)
# a4: tf.Tensor([-10  -6  -2   2   6], shape=(5,), dtype=int32)

