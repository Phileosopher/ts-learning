import tensorflow as tf
import numpy as np

pred = np.array([[31, 23,  4, 24, 27, 34],
                [18,  3,  25,  0,  6, 35],
                [28,  14, 33, 22, 20,  8],
                [13,  30, 21, 19,  7,  9],
                [16,  1,  26, 32,  2, 29],
                [17,  12, 5,  11, 10, 15]])

y =    np.array([[31, 23,  4, 24, 27, 14],
                [18,  3,  25,  0,  6, 35],
                [28,  14, 33, 22, 20,  8],
                [13,  30, 21, 19,  7,  9],
                [16,  1,  26, 32,  2, 29],
                [17,  12,  5, 11, 10, 15]])

prediction = tf.equal(tf.argmax(input=pred,axis=1),tf.argmax(input=y,axis=1))
accuracy = tf.reduce_mean(input_tensor=tf.cast(prediction, tf.float32))

print("prediction:",prediction)
print("accuracy:  ",accuracy)

# prediction: tf.Tensor([False  True  True  True  True  True], shape=(6,), dtype=bool)
# accuracy:   tf.Tensor(0.8333333, shape=(), dtype=float32)

