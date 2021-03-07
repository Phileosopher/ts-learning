import numpy as np
from itertools import product
import matplotlib.pyplot as plt

points = np.array(list(product(range(3),range(4))))

plt.plot(points[:,0],points[:,1],'ro')
plt.show()
