import array
import copy
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.ndimage import zoom





# s1 = datetime.now()
data = np.random.randint(0, 256, size = (50, 50, 521)).astype(np.uint8)


def float_process(arr : np.ndarray) -> np.ndarray:
    return arr / 255

def null_process(arr : np.ndarray) -> np.ndarray:
    for i in range(len(arr)):
        arr[i] = np.NaN if arr[i] < 0.9 else arr[i]
    return arr

def resize_3D(Data : np.ndarray, x_factor=1, y_factor=1, z_factor=1) -> np.ndarray:
    return zoom(Data, (x_factor, y_factor, z_factor))

def view(Data):
    # 3D-Data : shape[x, y, z]

    x = np.arange(Data.shape[0])
    y = np.arange(Data.shape[1])
    z = np.arange(Data.shape[2])

    k = np.meshgrid(x, y, z)

    c = Data.reshape(-1)
    # print(len(c))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # ax = plt.gcf().gca(projection="3d")

    ax.scatter(xs=k[0], ys=k[1], zs=k[2], c=c, s=1, cmap="gray")
    ax.view_init(200, 240)

    ax.set_xlabel('X', color='r')
    ax.set_ylabel('Y', color='g')
    ax.set_zlabel('Z', color='b')

    plt.show()



arr = data.reshape(-1)
print(arr.shape)
print(data.shape)


d_data = copy.deepcopy(arr)


d_data = null_process(resize_3D(float_process(d_data).reshape(50, 50, 521), 1, 1, 200/521).reshape((-1)))

d_data = d_data.reshape(50, 50, -1)

print(d_data.shape)

view(d_data)




# 문제!!!!!!!!!!!!!!!
# resize 후에 널처리 해야 연산이 제대로 된다...
# NULL 연산 불가.... --->>>>> resize 불가