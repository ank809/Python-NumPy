# To initialize an array with all zeros
import numpy as np
a= np.zeros((2, 3), dtype="int32")
print(a)

# To initialize an array with all ones
b=np.ones((4, 3, 2), dtype="int32")
print(b)

# To initialize an array of a specific number
c= np.full((2, 4), 21)
print(c)

# To initialize an array like another array
d= np.full_like(a, 14)
# you can do the same by this also
e= np.full(a.shape, 14)
print(d)
print(e)

# To make an array of random numbers

# f= np.random.rand((2, 3)) can't do like this
f= np.random.rand(2, 3)
print(f)

# to make a random array like another array
g= np.random.random_sample(c.shape)
print(g)


# Random matrix of integer type
h= np.random.randint(1, 8, size=(3,3))
print(h)

# An identity matrix
i= np.identity(4, dtype="int32")
print(i)

# To repeat an array
i= np.repeat([[1, 2, 3]], 3, axis=0)
j= np.repeat([[2, 3, 4]], 2, axis=0)
print(i)
print(j)