import tensorflow as tf 

aconst = tf.constant(3.0)
print(aconst)

# Automatically close "sess"
with tf.Session() as sess:
  print(sess.run(aconst)) 

