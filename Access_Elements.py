# To access elements in an array
import numpy as np
arr= np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr)

# To access a particular row i.e 3
print("Third row is ", arr[2, :])

# To access a particular column i.e 3
print("Third column is", arr[:, 2])

# To change a whole row i.e 2
arr[1, :]=0
print(arr)

# To change a whole column i.e 3
arr[:, 2]=1
print(arr)

# To change whole column but in sequence or particular numbers

arr[:, 2]= [2, 0, 2]
print(arr)

# If you want to print only specific characters of a row
a= np.array([[1, 2, 3, 4 ,5 ,6, 7],[8, 9,10,11,12, 13, 14]])
print(a)

# Print only 2, 4, 6
# [startIndex:endIndex:stepSize]
print(a[0, 1:6:2])

# Print only 8, 10, 12, 14
print(a[1, ::2])

# Print only 5, 12
print(a[:, 4])
