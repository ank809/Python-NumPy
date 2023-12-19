# Numpy is a library for arrays in Python.
# NumPy stands for Numerical Python.
# In Python, we have lists that serve the purpose of arrays, but they are slow to process.
# Lists store :
# 1. Size 4bytes
# 2. Object count 8bytes
# 3. Object value 8bytes
# 4. Reference Count 8bytes
# while the array in numpy takes 4 bytes only and due to of this reason it is much more faster than lists
# Numpy only store variable of same type while lists can store any type of var
# Numpy utilizes contiguous memory while lists do not

import numpy as np
print(np.__version__)
a= np.array([1, 2, 3])
print(a)
b= np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(b)
print(a[2])
print(b[2, 2])
print(a.ndim)
# Shows the dimension of the array
print(b.ndim)
# To get shape of array
print(a.shape)
print(b.shape)
# To get itemsize
print(a.itemsize)
print(b.itemsize)
# To get datatype
print(a.dtype)
print(b.dtype)

# To get specific row
print(b[0,:])   #(row, column)
print(b[:,1])

# changing elements of array
b[1:3, 1:3]=0
print(b)