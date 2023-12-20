import numpy as np
a= np.random.randint(1, 100, 24).reshape(4, 6)
print(a)

# find all number greater than 50

print("Numbers greater than 50 are: ",a[a>50])

# number greater than 50 and are even

print("Numbers greater than 50 and even are: ", a[(a>50) & (a%2==0)])

print("Numbers not divisible by 7 are: ", a[a%7!=0])

print("Numbers not divisible by 7 are: ", a[~(a%7==0)])
