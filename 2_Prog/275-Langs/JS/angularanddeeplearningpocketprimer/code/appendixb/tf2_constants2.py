import tensorflow as tf # tf2-variables.py

x = tf.constant(5,name="x")
y = tf.constant(8,name="y")

@tf.function
def calc_prod(x, y):
  z = 2*x + 3*y
  return z

result = calc_prod(x, y)
print('result =',result)

