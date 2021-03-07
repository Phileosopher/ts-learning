import numpy as np
import matplotlib.pyplot as plt

apples  = 500
bananas = 500

grey_height = 28 + 4 * np.random.randn(apples)
labs_height = 24 + 4 * np.random.randn(bananas)

plt.hist([grey_height, labs_height],stacked=True,color=['r','b'])
plt.show()

