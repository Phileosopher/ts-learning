import numpy as np
import matplotlib.pyplot as plt

x = [7,11,13,15,17,19,23,29,31,37]

plt.plot(x) # OR: plt.plot(x, ‘ro-’) or bo
plt.ylabel(’Height')
plt.xlabel(’Weight')
plt.show()

