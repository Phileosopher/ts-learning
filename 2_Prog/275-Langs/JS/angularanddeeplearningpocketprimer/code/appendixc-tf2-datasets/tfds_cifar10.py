import tensorflow as tf
import tensorflow_datasets as tfds

loader = tfds.load("cifar10", as_supervised=True)
train, test = loader["train"], loader["test"]

train = train.map(
  lambda image, label: (tf.image.convert_image_dtype(image, tf.float32), label)
).cache().map(
  lambda image, label: (tf.image.random_flip_left_right(image), label)
).map(
  lambda image, label: (tf.image.random_contrast(image, lower=0.0, upper=1.0), label)
).shuffle(100).batch(64).repeat()

