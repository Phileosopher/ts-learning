import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# X range
x_vals = np.linspace(start=-10., stop=10., num=100)

# ReLU activation
print(tf.nn.relu([-3., 3., 10.]))
y_relu = tf.nn.relu(x_vals)

# ReLU-6 activation
print(tf.nn.relu6([-3., 3., 10.]))
y_relu6 = tf.nn.relu6(x_vals)

# Sigmoid activation
print(tf.nn.sigmoid([-1., 0., 1.]))
y_sigmoid = tf.nn.sigmoid(x_vals)

# Hyperbolic Tangent activation
print(tf.nn.tanh([-1., 0., 1.]))
y_tanh = tf.nn.tanh(x_vals)

# Softsign activation
print(tf.nn.softsign([-1., 0., 1.]))
y_softsign = tf.nn.softsign(x_vals)

# Softplus activation
print(tf.nn.softplus([-1., 0., 1.]))
y_softplus = tf.nn.softplus(x_vals)

# Exponential linear activation (ELU)
print(tf.nn.elu([-1., 0., 1.]))
y_elu = tf.nn.elu(x_vals)

# Plot the different functions
plt.plot(x_vals, y_softplus, 'r--', label='Softplus', linewidth=2)
plt.plot(x_vals, y_relu, 'b:', label='ReLU', linewidth=2)
plt.plot(x_vals, y_relu6, 'g-.', label='ReLU6', linewidth=2)
plt.plot(x_vals, y_elu, 'k-', label='ExpLU', linewidth=0.5)
plt.ylim([-1.5,7])
plt.legend(loc='best')
plt.show()

plt.plot(x_vals, y_sigmoid, 'r--', label='Sigmoid', linewidth=2)
plt.plot(x_vals, y_tanh, 'b:', label='Tanh', linewidth=2)
plt.plot(x_vals, y_softsign, 'g-.', label='Softsign', linewidth=2)
plt.ylim([-2,2])
plt.legend(loc='best')
plt.show()

