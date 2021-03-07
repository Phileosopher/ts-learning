import tensorflow as tf
import numpy as np

# cat, dog, bird, fish, carrot, apple
# predictions from our model:
pred = np.array([[0.1, 0.03, 0.2, 0.05, 0.02, 0.6],
                 [0.5, 0.04, 0.2, 0.06, 0.10, 0.1],
                 [0.2, 0.04, 0.5, 0.06, 0.10, 0.1]])

# true values from our labeled data:
y_vals = np.array([[0,  0,  0,  0,  0,  1],
                   [1,  0,  0,  0,  0,  0],
                   [0,  0,  1,  0,  0,  0]])

print("argmax(pred,1):  ", tf.argmax(input=pred,axis=1))
print("argmax(y_vals,1):", tf.argmax(input=y_vals,axis=1))

prediction = tf.equal(tf.argmax(input=pred, axis=1),tf.argmax(input=y_vals, axis=1))
accuracy = tf.reduce_mean(input_tensor=tf.cast(prediction, tf.float32))

print("prediction:",prediction)
print("accuracy:",accuracy)

# argmax(pred,1):   tf.Tensor([5 0 2], shape=(3,), dtype=int64)
# argmax(y_vals,1): tf.Tensor([5 0 2], shape=(3,), dtype=int64)
# prediction: tf.Tensor([ True  True  True], shape=(3,), dtype=bool)
# accuracy: tf.Tensor(1.0, shape=(), dtype=float32)

