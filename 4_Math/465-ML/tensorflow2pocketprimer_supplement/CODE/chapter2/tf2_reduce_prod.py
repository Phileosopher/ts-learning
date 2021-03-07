import tensorflow as tf

x = tf.constant([100,200,300], name="x")
y = tf.constant([1,2,3], name="y")

sum_x  = tf.reduce_sum(input_tensor=x, name="sum_x")
prod_y = tf.reduce_prod(input_tensor=y, name="prod_y")
div_xy = tf.math.divide(sum_x, prod_y, name="div_xy")

#div_xy = tf.compat.v1.div(sum_x, prod_y, name="div_xy")
# 'div' is deprecated in favor of operator or tf.math.divide

print("sum_x: ",sum_x)
print("prod_y:",prod_y)
print("div_xy:",div_xy)

# sum_x:  tf.Tensor(600, shape=(), dtype=int32)
# prod_y: tf.Tensor(6, shape=(), dtype=int32)
# div_xy: tf.Tensor(100, shape=(), dtype=int32)

