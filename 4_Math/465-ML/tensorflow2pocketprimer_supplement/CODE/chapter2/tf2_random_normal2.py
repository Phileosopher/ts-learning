import tensorflow as tf

for i in range(3):
  x_train = tf.random.normal((1,), mean=5, stddev=2.0)
  y_train = x_train * 2 + 3
  print("x_train:",x_train)
print("-----------------\n")

for i in range(3):
  x_train = tf.random.normal((2,), mean=5, stddev=2.0)
  y_train = x_train * 2 + 4
  print("x_train:",x_train)
print("-----------------\n")

for i in range(3):
  x_train = tf.random.normal((3,), mean=5, stddev=2.0)
  y_train = x_train * 2 + 6
  print("x_train:",x_train)
print("-----------------\n")

#x_train: tf.Tensor([5.056024], shape=(1,), dtype=float32)
#x_train: tf.Tensor([3.555944], shape=(1,), dtype=float32)
#x_train: tf.Tensor([2.5096486], shape=(1,), dtype=float32)
#x_train: tf.Tensor([6.3217654 6.1410522], shape=(2,), dtype=float32)
#x_train: tf.Tensor([7.323264 2.371657], shape=(2,), dtype=float32)
#x_train: tf.Tensor([5.8101373 5.4401507], shape=(2,), dtype=float32)
#x_train: tf.Tensor([3.0013518 1.8450763 6.2276907],shape=(3,),dtype=float32)
#x_train: tf.Tensor([9.014612  1.1454127 6.321906 ],shape=(3,),dtype=float32)
#x_train: tf.Tensor([6.7753267 7.2067122 5.665411 ],shape=(3,),dtype=float32)

