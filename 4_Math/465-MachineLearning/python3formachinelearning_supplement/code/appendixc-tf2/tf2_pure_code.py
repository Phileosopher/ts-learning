import tensorflow as tf

x = tf.Variable(1, 'float', name='w')

@tf.function
def calculate(x):
  y = x * 2
  return y

for x in range(3):
  result = calculate(x+1)
  print('y:',result)

