import tensorflow as tf

x = tf.constant([100,200,300], name='x')
y = tf.constant([1,2,3], name='y')

sum_x  = tf.reduce_sum(input_tensor=x, name="sum_x")
prod_y = tf.reduce_prod(input_tensor=y, name="prod_y")
mean   = tf.reduce_mean(input_tensor=[sum_x,prod_y], name="mean")

print("sum_x: ",sum_x)
print("prod_y:",prod_y)
print("mean:  ",mean)

# sum_x:  tf.Tensor(600, shape=(), dtype=int32)
# prod_y: tf.Tensor(6, shape=(), dtype=int32)
# mean:   tf.Tensor(303, shape=(), dtype=int32)

