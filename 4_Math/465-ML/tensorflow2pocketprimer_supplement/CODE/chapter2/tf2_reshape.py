import tensorflow as tf

x = tf.constant([[2,5,3,-5],[0,3,-2,5],[4,3,5,3]])

print("shape:  ",tf.shape(input=x))
print("shape 1:",tf.reshape(x, [6,2]))
print("shape 2:",tf.reshape(x, [3,4]))

# shape:   tf.Tensor([3 4], shape=(2,), dtype=int32)
# shape 1: tf.Tensor(
# [[ 2  5]
#  [ 3 -5]
#  [ 0  3]
#  [-2  5]
#  [ 4  3]
#  [ 5  3]], shape=(6, 2), dtype=int32)
# shape 2: tf.Tensor(
# [[ 2  5  3 -5]
#  [ 0  3 -2  5]
#  [ 4  3  5  3]], shape=(3, 4), dtype=int32)
 
