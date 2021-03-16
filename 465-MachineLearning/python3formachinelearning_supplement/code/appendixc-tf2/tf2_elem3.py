import tensorflow as tf

arr3 = tf.constant([[[1,2],[2,3]],[[3,4],[5,6]]])

#@tf.function  DO NOT USE THIS DECORATOR 
def compute_values():
  print('arr3:   ',arr3)
  print('[1]:    ',arr3[1])
  print('[1,1]:  ',arr3[1,1])
  print('[1,1,0]:',arr3[1,1,0])

compute_values()

