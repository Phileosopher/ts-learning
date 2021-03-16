import tensorflow as tf
import numpy as np

x = np.arange(0, 12)

def gener():
  i = 0 
  while(i < len(x/3)):
    yield (i, i+1, i+2)
    i += 3

ds = tf.data.Dataset.from_generator(gener, (tf.int64,tf.int64,tf.int64))

third = int(len(x)/3)
for value in ds.take(third):
  print("value:",value)

#value: (<tf.Tensor: id=34, shape=(), dtype=int64, numpy=0>, <tf.Tensor: id=35, shape=(), dtype=int64, numpy=1>, <tf.Tensor: id=36, shape=(), dtype=int64, numpy=2>)
#value: (<tf.Tensor: id=40, shape=(), dtype=int64, numpy=3>, <tf.Tensor: id=41, shape=(), dtype=int64, numpy=4>, <tf.Tensor: id=42, shape=(), dtype=int64, numpy=5>)
#value: (<tf.Tensor: id=46, shape=(), dtype=int64, numpy=6>, <tf.Tensor: id=47, shape=(), dtype=int64, numpy=7>, <tf.Tensor: id=48, shape=(), dtype=int64, numpy=8>)
#value: (<tf.Tensor: id=52, shape=(), dtype=int64, numpy=9>, <tf.Tensor: id=53, shape=(), dtype=int64, numpy=10>, <tf.Tensor: id=54, shape=(), dtype=int64, numpy=11>)
