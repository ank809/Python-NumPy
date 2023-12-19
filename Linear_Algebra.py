import numpy as np
a= np.array([[1, 2,3],[ 4,5,6]])
print(a)
print(a.shape)

b= np.array([[1,2],[3,4],[5,6]])
print(b)
print(b.shape)

# the matmul function multiply two arrays while * multiplies the adjacent element in matrices
# To multiply two matrices using matmul function the row of first matrix should be equal to column of
# 2nd matrix
print(np.matmul(a,b))

c=np.identity(3)
print(np.linalg.det(c))
