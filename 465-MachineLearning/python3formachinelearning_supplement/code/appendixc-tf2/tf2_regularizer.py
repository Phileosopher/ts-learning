import tensorflow as tf

W = tf.Variable(tf.ones(shape=(2,2)), name="W")
b = tf.Variable(tf.zeros(shape=(2)), name="b")

@tf.function
def forward(x):
  return W * x + b

x = forward([1,0])
print("x:",x)

# L2 regularizer
l2_regularizer = tf.keras.regularizers.l2(0.04)
loss = l2_regularizer(W)

print("loss:",loss)

