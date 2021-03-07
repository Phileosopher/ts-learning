import numpy as np
 
x_data = np.linspace(-1, 1, 11)
y_data = 4*x_data + np.random.randn(*x_data.shape)*0.5

print("x_data: ",x_data)
print("y_data: ",y_data)

