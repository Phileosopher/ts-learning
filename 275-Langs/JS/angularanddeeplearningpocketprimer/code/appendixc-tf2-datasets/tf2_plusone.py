import tensorflow as tf
import numpy as np

x = np.arange(0, 10)

def gener():
  for i in x:
    yield (i+1)

ds = tf.data.Dataset.from_generator(gener, (tf.int64))

for value in ds.take(len(x)):
  print("1value:",value)

for value in ds.take(2*len(x)):
  print("2value:",value)

