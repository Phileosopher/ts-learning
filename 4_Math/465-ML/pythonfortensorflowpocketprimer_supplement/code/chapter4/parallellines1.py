import matplotlib.pyplot as plt
import numpy as np

# lower line 
x1 = np.linspace(-5,5,num=200)
y1 = 2*x1 

# upper line 
x2 = np.linspace(-5,5,num=200)
y2 = 2*x2 + 3

# horizontal axis 
x3 = np.linspace(-5,5,num=200)
y3 = 0*x3 + 0

# vertical axis 
plt.axvline(x=0.0)

plt.axis([-5, 5, -10, 10])
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.show()

