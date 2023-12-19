# 3-D Array in NumPy is like a set of tables.
# It has 3 parameters (tables, rows, columns)
# We can also say that 3-d array is a collection of 2-d arrays

# Create a 3-D array of dimension 2, 3, 2
# 2, 3, 2 can be written as 2, (3, 2). Here (3, 2) this is our 2-d array and for understanding simply just
# make (3, 2) array 2 times and that will be a 3-d array

import numpy as np
arr= np.array([
    [[1, 2],[3, 4],[5, 6]],
    [[7, 8],[9, 10],[11, 12]]
])
print(arr)

print(arr.ndim)

print(arr.shape)

print(arr.size)

print(arr.dtype)

print(arr.itemsize)

# To access particular elements of 3-D array i.e 9
print(arr[1, 1, 0])

# access 12
print(arr[1, 2, 1])

# access 3
print(arr[0, 1, 0])

# Change elements of array 1, 2, 3, 4=0
arr[0,:2, : ]=0
print(arr)

# Change 9, 10, 11, 12 to 1
arr[1,1:3, : ]=1
print(arr)
