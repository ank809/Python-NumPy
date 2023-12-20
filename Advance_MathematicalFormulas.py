# To calculate Sigmoid of a array. Sigmoid takes numbers in between 0-1
# S(x)= 1/1+e^-x
import numpy as np


def sigmoid(array):
    return 1 / (1 + np.exp(-array))


a = np.arange(10)
print(a)
print(sigmoid(a))

# Mean squared error: Error between the actual and the predicted value i.e. given by system
# (actual-predicted)^2
b= np.random.randint(1, 50, 25)
c= np.random.randint(1, 50, 25)
print(b)
print(c)

def mse(actual, predicted):
    print((actual - predicted) ** 2)
    return np.mean((actual-predicted)**2)


print(mse(b,c))