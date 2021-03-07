import tensorflow as tf

x1  = tf.constant([0.9, 2.5, 2.3, -4.5])
x2  = tf.constant([1.0, 2.0, 2.0, -4.0])
eq  = tf.equal(x1,x2)
neq = tf.not_equal(x1,x2)

print('x1: ',x1)
print('x2: ',x2)
print('eq: ',eq)
print('neq:',neq)

# x1:  tf.Tensor([ 0.9  2.5  2.3 -4.5], shape=(4,), dtype=float32)
# x2:  tf.Tensor([ 1.  2.  2. -4.], shape=(4,), dtype=float32)
# eq:  tf.Tensor([False False False False], shape=(4,), dtype=bool)
# neq: tf.Tensor([ True  True  True  True], shape=(4,), dtype=bool)

