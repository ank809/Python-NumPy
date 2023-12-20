# Execution time taken by NumPy and Lists in Python

# List in Python
a= [i for i in range (10000000)]
b= [i for i in range (10000000, 20000000)]

c=[]
import time
start1= time.time()

for i in range (len(a)):
    c.append(a[i]+b[i])
print(time.time()-start1)


# NumPy
import numpy as np
a= np.arange(10000000)
b=np.arange(10000000, 20000000)
start2= time.time()
c=a+b
print(time.time()-start2)

print(time.time())

print((start1/start2)*100)
# NumPy store elements in direct memory whereas lists give reference and numpy array is static while lists are
# dynamic in nature
