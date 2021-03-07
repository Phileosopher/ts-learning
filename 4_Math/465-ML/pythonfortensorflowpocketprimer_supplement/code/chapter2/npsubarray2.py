import numpy as np

arr1  = np.array([1,2,3,4,5])
print('arr1:',arr1)

print('arr1[0:-1]:',arr1[0:-1])
print('arr1[1:-1]:',arr1[1:-1])
print('arr1[::-1]:',arr1[::-1])

#('arr1:',       array([1, 2, 3, 4, 5]))
#('arr1[0:-1]:', array([1, 2, 3, 4]))
#('arr1[1:-1]:', array([2, 3, 4]))
#('arr1[::-1]:', array([5, 4, 3, 2, 1]))

