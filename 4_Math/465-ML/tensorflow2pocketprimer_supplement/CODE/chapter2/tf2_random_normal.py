import tensorflow as tf 

# initialize a 6x3 array of random numbers:
values = {'weights':tf.Variable(tf.random.normal([6,3]))}

print("values:")
print(values['weights'])

