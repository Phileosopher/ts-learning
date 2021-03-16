import tensorflow as tf 

aconst = tf.constant(3.0)
print(aconst)
# output: Tensor("Const:0", shape=(), dtype=float32)

sess = tf.Session()  
print(sess.run(aconst))
# output: 3.0

sess.close()
# => there's a better way…

