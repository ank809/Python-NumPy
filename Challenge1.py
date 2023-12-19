# [
#     [1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 1],
#     [1, 0, 9, 0, 1],
#     [1, 0, 0, 0, 1],
#     [1, 1, 1, 1 ,1]
# ] Create this matrix

import numpy as np
a= np.ones((5, 5), dtype="int32")
# print(a)
a[1, 1:4]=0
a[3, 1:4]=0
# print(a)
a[2, 1::2]=0
# print(a)
a[2, 2]=9
print(a)

# Important Note:
# When we copy one array to another then if we change one then other will also be changed
a= np.array([1, 2, 3])
# b=a
# b[0]=100
# As we have changed b so a will also be changes to prevent this
b=a.copy()
b[0]=100
print(a)
print(b)