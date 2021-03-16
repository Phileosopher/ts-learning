import numpy as np

x2 = np.arange(8)
print 'mean = ',x2.mean()
print 'std  = ',x2.std()

x3 = (x2 - x2.mean())/x2.std()
print 'x3 mean = ',x3.mean()
print 'x3 std  = ',x3.std()

