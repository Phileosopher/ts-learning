import numpy as np
import pylab
from itertools import product
import matplotlib.pyplot as plt

fig = pylab.figure()    
ax = fig.add_subplot(1,1,1)

ax.grid(which='major', axis='both', linestyle='--')

[line.set_zorder(3) for line in ax.lines]
fig.show() # to update

plt.gca().xaxis.grid(True)
plt.show()

