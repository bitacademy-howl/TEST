import numpy as np
from scipy.signal import butter, filtfilt, hilbert
from matplotlib import pyplot as plt


def FilteredSignal(signal, fs, cutoff):
    B, A = butter(1, cutoff / (fs / 2), btype="low")
    filtered_signal = filtfilt(B, A, signal, axis=0)
    return filtered_signal

fs = 10000.
T = .1
time = np.arange(0., T, 1 / fs)
frequency = 1000
noise = np.random.normal(0, 1, int(fs/10))
signal = np.sin(2 * np.pi * frequency * time) + 0.2 * noise

cutoff = 1000
filteredSignal = FilteredSignal(signal, fs, cutoff=cutoff)

analyticSignal = hilbert(filteredSignal)
amplitudeEnvelope = np.abs(analyticSignal)

fig, ax = plt.subplots(1, 1)
ax.plot(time, signal)
ax.plot(time, filteredSignal)
ax.plot(time, amplitudeEnvelope)
ax.set_xlabel("Tiempo")
ax.set_ylabel("Amplitud")
ax.grid(True)
plt.show()








def fft_sig(data, Fs):
    n = len(data)
    NFFT = n

    k = np.arange(NFFT)
    f0 = k*Fs / NFFT




Fs = 80e6
T = 1 / Fs
te = 0.5
t = np.arange(0, te, T)
noise = np.random.normal(0, 50, len(t))
x = 0.6*np.cos(2 * np.pi * 60 * t + np.pi/2) + np.cos(2*np.pi * 120 * t)

y = x



# plt.figure(num=1, dpi=100, facecolor="white")
plt.figure()
plt.plot(t,y,"r")
plt.xlim(0, 0.05)
plt.xlabel("time($sec$")
plt.ylabel("y")
plt.show()

# plt.savefig("./test_figure1.png", dpi=300)

#
# def FilteredSignal(signal, fs, cutoff):
#     B, A = butter(1, cutoff / (fs / 2), btype="low")
#     filtered_signal = filtfilt(B, A, signal, axis=0)
#     return filtered_signal
#
# fs = 10000.
# T = .1
# time = np.arange(0., T, 1 / fs)
# frequency = 1000
# noise = np.random.normal(0, 1, int(fs/10))
# signal = np.sin(2 * np.pi * frequency * time) + 0.2 * noise
# analyticSignal = hilbert(signal)
# amplitudeEnvelope = np.abs(analyticSignal)
#
# cutoff = 1000
# filteredSignal = FilteredSignal(amplitudeEnvelope, fs, cutoff=cutoff)
# fig, ax = plt.subplots(1, 1)
# ax.plot(time, signal)
# ax.plot(time, filteredSignal)
# ax.set_xlabel("Tiempo")
# ax.set_ylabel("Amplitud")
# ax.grid(True)
# plt.show()
