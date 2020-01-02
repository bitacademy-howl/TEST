# -*- coding: utf-8 -*-

def toHz(value):
    from numpy import pi
    return value / 2 / pi


def direct2FormModel(data, a1, a2, b0, b1, b2):
    from numpy import zeros, arange

    result = zeros((len(data),))
    timeZone = zeros((len(data),))

    for n in arange(2, len(data)):
        sum0 = -a1 * timeZone[n - 1] - a2 * timeZone[n - 2]
        timeZone[n] = data[n] + sum0
        result[n] = b0 * timeZone[n] + b1 * timeZone[n - 1] + b2 * timeZone[n - 2]

    return result


def differentialEqForm(data, a1, a2, b0, b1, b2):
    from numpy import zeros, arange

    result = zeros((len(data),))

    for n in arange(2, len(data)):
        result[n] = b0 * data[n] + b1 * data[n - 1] + b2 * data[n - 2] - a1 * result[n - 1] - a2 * result[n - 2]

    return result


def filterSimpleLPF(data, tau, Ts):
    from numpy import zeros, arange

    result = zeros((len(data),))

    for n in arange(1, len(data)):
        result[n] = (tau * result[n - 1] + Ts * data[n]) / (tau + Ts)

    return result


def draw_FFT_Graph(data, fs, **kwargs):
    from numpy.fft import fft
    import matplotlib.pyplot as plt

    graphStyle = kwargs.get('style', 0)
    xlim = kwargs.get('xlim', 0)
    ylim = kwargs.get('ylim', 0)
    title = kwargs.get('title', 'FFT result')

    n = len(data)
    k = np.arange(n)
    T = n / Fs
    freq = k / T
    freq = freq[range(int(n / 2))]
    FFT_data = fft(data) / n
    FFT_data = FFT_data[range(int(n / 2))]

    plt.figure(figsize=(12, 5))
    if graphStyle == 0:
        plt.plot(freq, abs(FFT_data), 'r', linestyle=' ', marker='^')
    else:
        plt.plot(freq, abs(FFT_data), 'r')
    plt.xlabel('Freq (Hz)')
    plt.ylabel('|Y(freq)|')
    plt.vlines(freq, [0], abs(FFT_data))
    plt.title(title)
    plt.grid(True)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.show()


import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

# Create Test Signal
Fs = 20 * 10 ** 3  # 20kHz
Ts = 1 / Fs  # sample Time
endTime = 2
t = np.arange(0.0, endTime, Ts)

inputSig = 3. * np.sin(2. * np.pi * t)

sampleFreq = np.arange(10, 500, 50)

for freq in sampleFreq:
    inputSig = inputSig + 2 * np.sin(2 * np.pi * freq * t)

plt.figure(figsize=(12, 5))
plt.plot(t, inputSig)
plt.xlabel('Time(s)')
plt.title('Test Signal in Continuous')
plt.grid(True)
plt.show()

draw_FFT_Graph(inputSig, Fs, title='inputSig', xlim=(0, 500))

# Design 1st Order Low Pass Filter
f_cut = 100
w_cut = 2 * np.pi * f_cut
tau = 1 / w_cut

num = np.array([1.])
den = np.array([tau, 1.])
w, h = sig.freqs(num, den, worN=np.logspace(0, 5, 1000))

plt.figure(figsize=(12, 5))
plt.semilogx(toHz(w), 20 * np.log10(abs(h)))
plt.axvline(f_cut, color='k', lw=1)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude response [dB]')
tmpTitle = 'Low Pass Filter, cutoff freq. at ' + str(f_cut) + 'Hz in continuous'
plt.title(tmpTitle)
plt.xlim(1, Fs / 2)
plt.grid()
plt.show()

# Design 1st Order Low Pass Filter Z-Transform
num_z = np.array([Ts / (tau + Ts)])
den_z = np.array([1., -tau / (tau + Ts)])

wz, hz = sig.freqz(num_z, den_z, worN=10000)

plt.figure(figsize=(12, 5))
plt.semilogx(toHz(wz * Fs), 20 * np.log10(abs(hz)), 'r', label='discrete time')
plt.semilogx(toHz(w), 20 * np.log10(abs(h)), 'b--', label='continuous time')
plt.axvline(f_cut, color='k', lw=1)
plt.axvline(Fs / 2, color='k', lw=1)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude response [dB]')
tmpTitle = 'Low Pass Filter, cutoff freq. at ' + str(f_cut) + 'Hz in discrete'
plt.title(tmpTitle)
plt.xlim(1, Fs / 2)
plt.grid()
plt.legend()
plt.show()

# Implementation Signal
a1 = den_z[1]
a2 = 0
b0 = num_z[0]
b1 = 0.
b2 = 0.

filteredSig1 = filterSimpleLPF(inputSig, tau, Ts)
filteredSig2 = differentialEqForm(inputSig, a1, a2, b0, b1, b2)
filteredSig3 = direct2FormModel(inputSig, a1, a2, b0, b1, b2)

draw_FFT_Graph(filteredSig1, Fs, title='filterSimpleLPF', xlim=(0, 500))
draw_FFT_Graph(filteredSig2, Fs, title='differentialEqForm', xlim=(0, 500))
draw_FFT_Graph(filteredSig3, Fs, title='direct2FormModel', xlim=(0, 500))

plt.figure(figsize=(12, 5))
plt.plot(t, inputSig)
plt.plot(t, filteredSig1, 'r', label='SimpleLPF')
plt.plot(t, filteredSig2, 'c', label='DE')
plt.plot(t, filteredSig3, 'k', label='D2F')
plt.xlabel('Time(s)')
plt.title('Filtered Signal in Discrete')
plt.legend()
plt.grid(True)
plt.show()

# Err
err = filteredSig2 - filteredSig1
plt.figure(figsize=(12, 5))
plt.plot(t, err)
plt.xlabel('Time(s)')
plt.title('Error between differentialEqForm and filterSimpleLPF')
plt.grid(True)
plt.show()

err = filteredSig2 - filteredSig3
plt.figure(figsize=(12, 5))
plt.plot(t, err)
plt.xlabel('Time(s)')
plt.title('Error between differentialEqForm and direct2FormModel')
plt.grid(True)
plt.show()

err = filteredSig1 - filteredSig3
plt.figure(figsize=(12, 5))
plt.plot(t, err)
plt.xlabel('Time(s)')
plt.title('Error between filterSimpleLPF and direct2FormModel')
plt.grid(True)
plt.show()