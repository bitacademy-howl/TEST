from VO.DDD_python_3x import DDD_File

def get_data():
    ddd = DDD_File(path="./data/20191204original.ddd")
    ddd.Load()
    signal = np.array(ddd.GetData()[0:ddd.GetHeader().GetDepth()]) / 255
    return signal

import numpy as np
import matplotlib.pyplot as plt

fs = 100
t = np.arange(0, 3, 1 / fs)
f1 = 35
f2 = 10
signal = 0.6 * np.sin(2 * np.pi * f1 * t) + 3 * np.cos(2 * np.pi * f2 * t + np.pi / 2)

fft = np.fft.fft(signal) / len(signal)
fft_magnitude = abs(fft)




plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.grid()

length = len(signal)


plt.subplot(2, 1, 2)

# 1.
# plt.stem(fft_magnitude)
# 2.
f = np.linspace(-(fs / 2), fs / 2, length)
plt.stem(f, np.fft.fftshift(fft_magnitude), use_line_collection=True)

plt.ylim(0, 2.5)
plt.grid()

plt.show()