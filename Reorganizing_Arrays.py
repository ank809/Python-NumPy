import numpy as np
a= np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print(a)
print(a.shape)
b= a.reshape((8,1))
print(b)
b= a.reshape((8,1))
print(b)
b= a.reshape((4, 2))
print(b)
b=a.reshape((2, 2, 2 ))
print(b)

# Two combine two arrays or Vertically stacking arrays on top of each other
v1= np.array([1, 2, 3, 4])
v2= np.array([5, 6, 7, 8])

print(np.vstack([v1, v2]))
print(np.vstack([v1, v2, v2, v2]))

print(np.hstack([v1, v2]))

h1= np.ones((2, 4))
h2= np.zeros((2, 2))
h=np.hstack([h1, h2])
print(h)
print(h.shape)


# Assuming "data.txt" contains comma-separated numbers
filetext = np.genfromtxt("data.txt", delimiter=",")

print(filetext)

file= filetext.astype("int32")
print(file)

print(file >50)

print(file[file>50])

print((file>50)&(file<100))

print(~(file>50)&(file<100))