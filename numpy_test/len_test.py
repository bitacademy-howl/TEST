import numpy as np


WIDTH = 2
HEIGHT = 2
narr = np.array([1,2,3,4,5,6,7,8,9,10,11,12], dtype=np.float)

DEPTH = int(len(narr)/(WIDTH*HEIGHT))

print(DEPTH)

for i in range(WIDTH*HEIGHT):
    bias = i * DEPTH
    buf = narr[bias:bias + DEPTH]
    print(buf)

