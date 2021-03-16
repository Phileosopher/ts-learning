import matplotlib.pyplot as plt
import numpy as np

# top line 
x1 = np.linspace(-5,5,num=200)
y1 = 4 + 0*x1

# middle line 
x2 = np.linspace(-5,5,num=200)
y2 = 0 + 0*x2

# bottom line 
x3 = np.linspace(-5,5,num=200)
y3 = -3 + 0*x3

plt.axis([-5, 5, -5, 5])
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.show()

