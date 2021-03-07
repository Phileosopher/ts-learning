import tensorflow as tf

train, test = tf.keras.datasets.mnist.load_data()
mnist_x, mnist_y = train

mnist_ds = tf.data.Dataset.from_tensor_slices(mnist_x)
print(mnist_ds)

iterator = tf.compat.v1.data.make_one_shot_iterator(mnist_ds)

count = 0
max_count = 4

try:
  while True:
    print("value:",iterator.get_next())
    count += 1
    if(count > max_count):
      break
except tf.errors.OutOfRangeError:
  pass

