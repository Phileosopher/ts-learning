import tensorflow as tf

sess = tf.Session()

arr1 = tf.constant([1,2])
print('arr1: ',sess.run(arr1))
print('[0]:  ',sess.run(arr1)[0])
print('[1]:  ',sess.run(arr1)[1])

