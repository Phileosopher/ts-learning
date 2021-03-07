import tensorflow as tf

# normal distribution:
w = tf.Variable(tf.random.normal([784, 10], stddev=0.01))

# mean of an array:
b = tf.Variable([10,20,30,40,50,60],name='t')

print("w: ",w)
print("b: ",tf.reduce_mean(input_tensor=b))

