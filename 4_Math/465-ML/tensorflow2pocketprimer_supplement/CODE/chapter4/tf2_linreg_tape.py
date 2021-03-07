import tensorflow as tf
import matplotlib.pyplot as plt

step    = 20
rows    = 100
slope   = 0.4
bias    = 1.5

x_train = tf.random.uniform(shape=(rows,))
perturb = tf.random.normal(shape=(len(x_train),), stddev=0.01)
y_train = slope * x_train + bias + perturb

# initial values for slope 'm' and bias 'b'
m = tf.Variable(0.)
b = tf.Variable(0.)

# predict the y value based on a value for x 
def predict_y_value(x):
  y = m * x + b
  return y

# loss = RSS = residual sum of squares 
#      = sum of squares of difference 
#        between predicted and true values
def squared_error(y_pred, y_true):
  return tf.reduce_mean(tf.square(y_pred - y_true))

loss = squared_error(predict_y_value(x_train), y_train)
print("Initial loss:", loss.numpy())

######################################
# backward error propagation requires:
# a loss function (squared_error)
# an optimizer    (tape.gradient)
# a value for the learning rate 
# back propagation updates m and b
#####################################

learning_rate = 0.05
steps = 200

for i in range(steps):
  with tf.GradientTape() as tape:
    predictions = predict_y_value(x_train)
    loss = squared_error(predictions, y_train)
    
  gradients = tape.gradient(loss, [m, b])
  
  m.assign_sub(gradients[0] * learning_rate)
  b.assign_sub(gradients[1] * learning_rate)
  
  if(i % step) == 0:    
    print("Step %d, Loss %f" % (i, loss.numpy()))

# display trained values for slope m and bias b
print ("m: %f, b: %f" % (m.numpy(), b.numpy()))

