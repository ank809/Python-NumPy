# Missing values in Array
# How to make an array with some missing values
import numpy as np

# NaN values in Python are represented as float('nan') .
a = np.array([1, 2, 3, np.nan, 4, 5, 6, np.nan],)
print(a)

print(np.isnan(a))

print(a[~(np.isnan(a))])