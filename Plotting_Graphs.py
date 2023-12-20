import numpy as np
import matplotlib.pyplot as plt

# 2-D graph
# x=y i.e. straight line passing through origin at angle of 45
# x= np.linspace(-10, 10,100)
# print(x)
# y=x
# print(y)
# # dimension of x and y should be similar
# plt.plot(x,y)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Graph of y=x')
# plt.show()

# y=x^2 Graph of parabola
# x= np.linspace(-10, 10, 100)
# print(x)
# y= x**2
# print(y)
#
# plt.plot(x, y)
# plt.show()

# y=x^2 Graph of parabola
# y= np.linspace(-10, 10, 100)
# print(y)
# x= y**2
# print(x)
#
# plt.plot(x, y)
# plt.show()

# x=np.linspace(-10, 10, 100)
# print(x)
# y=np.sin(x)
# print(y)
#
# plt.plot(x,y)
# plt.show()

# x= np.linspace(-10, 10, 100)
# print(x)
# y=x*np.log(x)
# print(y)
#
# plt.plot(x,y)
# plt.show()

# Graph of sigmoid
x= np.linspace(-10, 10, 100)
print(x)
y=1/(1+np.exp(-x))
print(y)
plt.plot(x,y)
plt.show()