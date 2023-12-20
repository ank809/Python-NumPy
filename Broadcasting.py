# Broadcasting refers that how NumPy treats two different shapes array while doing arithematic operation
# The smaller array is broadcast along larger array so that they have compatible shapes.

# Steps:
# 1. Make both the array of same dimensions i.e. 2-d, 1-d, 3-d
# e.g: (3, 2) and other array is (3) then add 1 in head of smaller array i.e (1, 3)
# (3, 3, 2) and other is (2) then (1, 1, 2) is the new array

# 2. Make each dimension of two array of same size
# After make array with same dimension (3,3), (3), (1,3) stretch the 1 till the dimension do not become same
# (3,3)

import numpy as np
a= np.arange(12).reshape(4,3)
b= np.arange(3)
print(a)
print(b)
# here broadcasting will work, and you will not get any error i.e (4,3) (3)
# add head 1 in smaller array (1,3) then stretch the 1 of smaller array till it becomes of equal size (4,3)
# So here broadcasting will work
print(a+b)

# Suppose we take a (3,4) matrix and (3) matrix
a= np.arange(12).reshape(3, 4)
b= np.arange(3)
# print(a+b) could not be broadcast together with shapes (3,4) (3,)
# will get an error and Broadcasting will not work here,
# 1. (3,4) and (3) add 1 (1,3) then stretch 1 till the size of larger array (3,3)
# hence, (3,4) and (3,3) is not equal so you will get an error


c= np.arange(3).reshape(1,3)
d= np.arange(3).reshape(3,1)
print(c)
print(d)
print(c+d)


e= np.arange(3).reshape(1,3)
f= np.arange(4).reshape(4,1)
print(e)
print(f)
print(e+f)

e= np.arange(4).reshape(2,2)
f= np.arange(16).reshape(4,4)
print(e)
print(f)
# print(e+f)  will get an error

g= np.array([[1],[2]])
print(g)
print(g.shape)
h= np.array([[1],[2],[3]])
print(h)
print(h.shape)
# print(g+h) will get an error

i= np.arange(10)
print(i)
# To calculate sum of all the elements
print(np.sum(i))

# To calculate sin and cos of every element in array
print(np.sin(i))
print(np.cos(i))
