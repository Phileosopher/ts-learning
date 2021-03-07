import tensorflow as tf 

# initialize array of arrays:
a = [[1,2,3], [30,20,10], [40,60,50]]
b = tf.Variable(a, name='b')

print("b: ",tf.argmax(b,1))

