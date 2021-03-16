import tensorflow as tf

x = tf.ones((3, 3))
  
with tf.GradientTape() as t:
  t.watch(x)
  y = tf.reduce_sum(x)
  print("y:",y)
  z = tf.multiply(y, y)
  print("z:",z)
  z = tf.multiply(z, y)
  print("z:",z)

# the derivative of z with respect to y
dz_dy = t.gradient(z, y)
print("dz_dy:",dz_dy)

#In Listing 1.x, y equals the sum of the elements in the 3x3 tensor x, which is 9.
#Next, z is assigned the term y*y and then multiplied again by y, so the final expression fir z is here:
#z  = y*y*y
#z' = 3*y*y
#When z' is evaluated with the value 9 for y, the result is 3*9*9, which equals 243.

