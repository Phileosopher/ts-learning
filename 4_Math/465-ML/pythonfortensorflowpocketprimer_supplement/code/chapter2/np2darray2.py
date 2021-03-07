import numpy as np # np2darray2.py

arr1  = np.array([(1,2,3),(4,5,6),(7,8,9),(10,11,12)])

print('arr1:',arr1)
print('arr1[-1,:]:',arr1[-1,:])
print('arr1[:,-1]:',arr1[:,-1])
print('arr1[-1:,-1]:',arr1[-1:,-1])

#('arr1:',         array([[ 1,  2,  3],
#                         [ 4,  5,  6],
#                         [ 7,  8,  9],
#                         [10, 11, 12]]))

#('arr1[-1,:]:',   array([10, 11, 12]))
#('arr1[:,-1]:',   array([ 3,  6,  9, 12]))
#('arr1[-1:,-1]:', array([12]))

