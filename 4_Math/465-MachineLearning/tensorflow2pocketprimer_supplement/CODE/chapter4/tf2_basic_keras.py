import tensorflow as tf

# NOTE: we need the train data and test data

model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(1, activation=tf.nn.relu),
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#model.fit(x_train, y_train, epochs=5)
#model.evaluate(x_test, y_test)

