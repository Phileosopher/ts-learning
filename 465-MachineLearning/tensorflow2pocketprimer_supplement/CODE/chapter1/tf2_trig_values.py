import tensorflow as tf
import math as m

PI = tf.constant(m.pi)

a = tf.cos(PI/3.)
b = tf.sin(PI/3.)
c = 1.0/a # sec(60)
d = 1.0/tf.tan(PI/3.) # cot(60)

@tf.function
def math_values():
  print("a:",a) 
  print("b:",b) 
  print("c:",c) 
  print("d:",d) 

math_values()

