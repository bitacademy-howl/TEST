from scipy.signal import hilbert
from scipy_test.Data import get_data, FilteredSignal
import numpy as np
import matplotlib.pyplot as plt


fs = 80

signal = get_data()
t = np.arange(len(signal))




analytic_signal = hilbert(signal, N=None)
amplitude_envelope = np.abs(analytic_signal)

filteredSignal = FilteredSignal(signal, fs, cutoff=30)
analytic_signal2 = hilbert(filteredSignal, N=None)
amplitude_envelope2 = np.abs(analytic_signal2)





t = len(signal)
fs = 80e6
duration = len(signal) / fs
t = np.arange(0, duration, 1/fs)
t = t * 1e6  # t 의 단위 us로 변환


fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(t, signal, label="original")
ax1.plot(t, analytic_signal, label="analytic_signal")
ax1.plot(t, amplitude_envelope, label="enveloped")
ax1.legend()

ax2.plot(t, signal, label="original")
ax2.plot(t, filteredSignal, label="filteredSignal")
ax2.plot(t, analytic_signal2, label="analytic_signal")
ax2.plot(t, amplitude_envelope2, label="enveloped")
ax2.legend()

plt.show()
print("s")