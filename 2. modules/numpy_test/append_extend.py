import numpy as np
from numpy.core.multiarray import ndarray

WIDTH = 5
HEIGHT = 5
DEPTH = 20

x = ndarray(shape=[WIDTH, HEIGHT, DEPTH])

print(x[0][0], x[0][1], x[0][2])

z1 = np.array(range(20))
z2 = np.array(range(20, 40))
z3 = np.array(range(40, 60))

x[0][0] = z1
x[0][1] = z2
x[0][2] = z3

print(x[0][0], x[0][1], x[0][2])
print(x)

print(type(x), type(x[0]), type(x[0][0]), type(x[0][0][0]))