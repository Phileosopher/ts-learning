import tensorflow as tf
import numpy as np  

x1 = np.array([[1.,2.],[3.,4.]]) 
x2 = tf.convert_to_tensor(value=x1, dtype=tf.float32)

print ('x1:',x1)
print ('x2:',x2)

