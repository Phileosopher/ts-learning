import tensorflow as tf

sess = tf.Session()

arr3 = tf.constant([[[1,2],[2,3]],[[3,4],[5,6]]])
print('arr3:   ',sess.run(arr3))
print('[1]:    ',sess.run(arr3)[1])
print('[1,1]:  ',sess.run(arr3)[1,1])
print('[1,1,0]:',sess.run(arr3)[1,1,0])

