import numpy as np

# reorganizing  to form new array or stacking
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
arr2 = arr.reshape((8, 1))

print(arr)

# Stacking of arrays. should have same Dimensions to stack
# a=np.array([1,2,3])
# b=np.array([8,9,10])
# c=np.array([11,12])
# f=np.array([23,32])
# d=np.vstack((a,b))
# print(d)
#
# e=np.hstack((c,f))
# print(e)
