# Advanced Indexing is of 2 types
# 1. Integer Indexing
# 2. Boolean Indexing

# 1-d Array
import numpy as np
a=np.array([1, 2, 3, 4, 5, 6,7])
# access element 2, 4, 5
# Create an array of index of those element which you want to print
index=np.array([1, 3, 4])
print(a[index])

# Another way
print(a[[1, 3, 4]])

# Access elements in 2-d array
b=np.array([[1, 2, 3], [4, 5, 6]])
# print 3, 5
# rows of all the elements then column of all the elements you want to access
print(b[[0, 1],[2,1]])

# Access column 1
print(b[:, 1])

d= np.arange(0, 24).reshape(6, 4)
print("Array", d)
# access column 1, 3, 4
print(d[:, [0, 2, 3]])

# Boolean indexing
# c= np.arange(1,10).reshape(3,3)
# print(c)
# # This will display the numbers that are less than 5 . It is boolean indexing
# print(c[c<5])
#
# print(c[c>6])
