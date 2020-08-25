import numpy as np

# in Numpy we can access numpy as list
# a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# # print(a[[0,0,1,1],[0,1,2,3]])

filedata = np.genfromtxt("data.txt",delimiter=',')
filedata = filedata.astype('int32')
print(filedata)
# print(filedata > 50)
# print((filedata > 50) & (filedata<100))

print(np.any(filedata > 50,axis=0)) # use as np.all/np.any (cond,axis=0/1)