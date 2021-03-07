import tensorflow as tf

sess = tf.Session()

arr2 = tf.constant([[1,2],[2,3]])
print('arr2:  ',sess.run(arr2))
print('[1]:   ',sess.run(arr2)[1])
print('[1,1]: ',sess.run(arr2)[1,1])

