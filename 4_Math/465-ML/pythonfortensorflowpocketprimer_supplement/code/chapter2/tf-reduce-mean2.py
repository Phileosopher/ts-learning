import tensorflow as tf

x1 = tf.constant([[1,1,1],[2,2,2],[3,3,3],[4,4,4]], dtype=tf.float32)

y1 = tf.reduce_mean(x1, [0])
y2 = tf.reduce_mean(x1, [0,1])

sess = tf.Session()
print("y1:",sess.run(y1))
print("y2:",sess.run(y2))
sess.close()

