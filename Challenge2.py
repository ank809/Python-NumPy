import numpy as  np
a= np.ones((6, 5), dtype="int32")
print(a)
a[0, :]=[1, 2, 3, 4, 5]
a[1, :]=[6, 7, 8, 9, 10]
a[2, :]=[11, 12, 13, 14, 15]
a[3, :]=[16, 17, 18, 19, 20]
a[4, :]=[21, 22, 23, 24, 25]
a[5, :]=[26, 27, 28, 29, 30]

print(a)

a=np.arange(1, 31, dtype="int32").reshape((6, 5))
print(a)