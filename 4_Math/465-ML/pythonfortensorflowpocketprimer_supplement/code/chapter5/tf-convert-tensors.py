import tensorflow as tf
import numpy as np  

x_data = np.array([[1.,2.],[3.,4.]]) 
x = tf.convert_to_tensor(x_data, dtype=tf.float32)
print ('x1:',x)
sess = tf.Session() 
print('x2:',sess.run(x))

