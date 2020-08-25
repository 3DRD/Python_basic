"""
numpy is faster than list
Numpy uses fixed type
->faster uses less memory (def. int32-4bytes) while list(size-4,reference point-8,object type-8,object value-8 bytes)
->Contagious Memory everything stored in one block-better CPU,cache utilization
->does not check object type

lots more extra functions than lists

"""

import numpy as np

# a=np.array([1,2,3],dtype='int16')   # default int 32
# print(a)
# print(a.ndim)   # Gives dimension
# print(a.shape)  # Gives shape or rows x coloumns
# print(a.dtype)
# print(a.nbytes)     # Total number of bytes occupied by array
# print(a.size)       # Total number of items in array
# print(a.itemsize)   # Size of single item in array in bytes
#
# b=np.array([[1.0,2.0,3.0],[9.0,8.0,0.0]])
# print(b)
# print(b.ndim)
# print(b.shape)

# 3D array
# c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
#
# print(c.ndim)
# print(c)
# # replace
# c[:,1,:]=[[88,88],[99,99]]
# print(c)

# Array types
# d=np.ones((2,2))    # for array of all Ones
# e=np.zeros((2,2))   # for array of all zeros
# f=np.full((2,2),99) # for array of any given number
# g=np.full_like(a,4) # for array of any number of a certain shape can also use np.full(a.shape,4)
#
# print(d)
# print(e)
# print(g)

# for a matrix of random numbers between
# u=np.random.rand(4,4) # for matrix of row x col
# u=np.random.random_sample(a.shape)
# print(u)
# print(np.random.randint(-3,9,size=(3,3)))

# Identity Matrix
# print(np.identity(5))

# Repeat array
# arr=np.array([[1,2,3]])
# r1=np.repeat(arr,3,axis=0)
# print(r1)

"""!!!Careful while copying Numpy Array!!! Use  copy function """
# x=np.array([[1,1,1,1,1]])
# z=x.copy()
# y=np.repeat([[1,0,0,0,1]],3,axis=0)
# y[1,2]=9
# x=np.insert(x,1,y,axis=0)
# x=np.insert(x,4,z,axis=0)
# print(x)
#
# x=np.ones((5,5))
# z=np.zeros((3,3))
# z[1,1]=9
# x[1:4,1:4]=z
# print(x)

# Mathematical Functions
# a=np.array([1,2,3,4])
# a=a ** 2    # All mathematical functions
# print(np.sin(a))  # all Trigo Functions

# a = [0] * 5
# print(a)
# n=2
# m=3
# b = [0] * 5
# for i in range(n,m+1):
#     b[i] = 100
# a = a[a:b+1] + b[]
# print(a)
# def iterate(lst, start, end):
#   arr = []
#   if start < 0 or end >= len(lst) or start > end:
#      return
#   print(lst[start])
#   iterate(lst, start + 1, end)


# n=2
# m=7
# iterate([1,2,3,4,5,6,7,8,9,10],n-1,m-1)
# print(arr)

# a = a[1:3] + 100
# print(a)
# max = np.max(a)
# print(max)

scores = [[54, 67, 33, 44], [48, 99], [27]]
print(scores)
print(sum(scores[0][1:3]))
