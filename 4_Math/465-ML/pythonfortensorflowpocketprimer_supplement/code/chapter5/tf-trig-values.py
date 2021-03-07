import tensorflow as tf

import numpy as np
import math as m
PI = tf.constant(m.pi)

a = tf.cos(PI/3.)
b = tf.sin(PI/3.)
c = 1.0/a # sec(60)
d = 1.0/tf.tan(PI/3.) # cot(60)

with tf.Session() as sess:
  print('a:', sess.run(a))
  print('b:', sess.run(b))
  print('c:', sess.run(c))
  print('d:', sess.run(d))

