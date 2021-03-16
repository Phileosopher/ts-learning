# this code works with TensorFlow 2.1 and Python 3.6
import tensorflow as tf
import numpy as np

# get an instance of the TF 2 built-in mnist dataset:
mnist = tf.keras.datasets.mnist

# load the dataset into training and test:
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# compute the number of training labels:
num_labels = len(np.unique(y_train))

# make sure that all labels are one-hot encoded:
y_train = tf.keras.utils.to_categorical(y_train)
y_test  = tf.keras.utils.to_categorical(y_test)

# resize the training and test data x_train and x-test
# and then divide pixel values by 255 (normalization)
image_size = x_train.shape[1]
x_train = np.reshape(x_train,[-1, image_size, image_size])
x_test = np.reshape(x_test,[-1, image_size, image_size])
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# initialize some standard parameters:
input_shape = (image_size, image_size)
batch_size = 128
units = 256
dropout = 0.2

# create a Keras-based RNN model with:
# 256 units 
# input is 28-dimensional vector 
# having 28 timesteps
# with a few simple layers

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.SimpleRNN(units=units,
                    dropout=dropout,
                    input_shape=input_shape))
model.add(tf.keras.layers.Dense(num_labels))
model.add(tf.keras.layers.Activation('softmax'))
model.summary()

tf.keras.utils.plot_model(model, to_file='my-rnn-mnist.png', show_shapes=True)

# loss function for one-hot vector: sgd optimizer
# accuracy is good metric for classification tasks
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

# train the network: increase epochs for better results
model.fit(x_train, y_train, epochs=5, batch_size=batch_size)

loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))
