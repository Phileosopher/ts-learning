import tensorflow as tf
import numpy as np

x = np.random.sample((8,2))
size = x.shape[0]

def gener():
  for i in range(0,size):
    yield (x[i][0], x[i][1])

ds = tf.data.Dataset.from_generator(gener, (tf.float64,tf.float64))

for value in ds:
  print("value:",value)

