from scipy.signal import butter
from Signal_Process.DAO import GetSimpleSignal
import numpy as np
import matplotlib.pyplot as plt
import scipy
from Signal_Process.DAO import GetData
from Signal_Process.Wave_Process import Processor, Filter


def test1():
    signal = GetData()
    resampled = scipy.signal.resample(signal, int(len(signal)*5))
    print(len(resampled))


    # figure 설정
    fig = plt.figure()
    ax1 = fig.add_subplot(4,1,1)
    ax4 = fig.add_subplot(4,1,2)
    ax2 = fig.add_subplot(4,1,3)
    ax3 = fig.add_subplot(4,1,4)

    ax1.plot(signal)
    ax4.plot(resampled)
    # signal fft

    fft_magnitude = Processor.fft(signal)
    fft_result = np.fft.fftshift(fft_magnitude)

    # ax2.stem(fft_magnitude)
    fs = 80e6
    # f = np.linspace(-(fs / 2), (fs / 2), len(signal)*5)
    f = np.linspace(-(fs / 2), (fs / 2), len(signal))
    ax2.plot(f, fft_result)
    ax2.grid()

    reverse = Processor.rfft(fft_result)
    ax3.plot(reverse)

    plt.show()

def SimpleSignalMake():

    sig1, sig2, t = GetSimpleSignal()
    fig = plt.figure()
    ax2 = fig.add_subplot(612)
    ax2.plot(t, sig1, label='signal1')
    ax2.plot(t, sig2, label='signal2')
    ax2.set_xlabel("time in seconds")
    ax2.legend()
    plt.show()

def filter_main():
    f = Filter()
    sig = SimpleSinusoidal()
    f.LPF(sig)

def SimpleSignalFFT():
    sig1, sig2, t = GetSimpleSignal()
    fft_magnitude, fft_result = Processor.fft(sig1)
    plt.stem(fft_result)
    plt.show()

def SimpleSinusoidal(f=30e6, fs=30e6*20, duration=100/30e6):
    t = np.arange(0, duration, 1/fs)
    sin = np.sin(2*np.pi*f*t)
    cos = np.sin(2 * np.pi * f * t)
    return sin, cos



def SignalAnalizeView(signal, duration, fs):
    # fs = sample/sec
    # duration = sec

    t = np.arange(0, duration, 1/fs)

    magnitude, spectrum = Processor.fft(signal)
    result_signal = Processor.rfft(spectrum)

    print(len(signal), len(result_signal), len(magnitude), len(spectrum))

    fig = plt.figure()
    ax1 = fig.add_subplot(3, 1, 1)
    ax2 = fig.add_subplot(3, 1, 2)
    ax3 = fig.add_subplot(3, 1, 3)

    ax1.plot(t, signal, label = "orignal")
    ax1.set_xlabel('Time(Sec)')
    ax1.set_ylabel('Level')
    ax1.grid(True)
    ax1.legend(loc="upper right")

    result = result_signal[0, len(t)-1]
    ax1.plot(t, result, label = "result")
    ax1.set_xlabel('Time(Sec)')
    ax1.set_ylabel('Level')
    ax1.grid(True)
    ax1.legend(loc="upper right")

    f = np.linspace(-(fs / 2), (fs / 2), len(spectrum))
    ax2.plot(f, spectrum)
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('Gain')
    ax2.grid(True)
    ax2.legend(loc="upper right")

    plt.show()



    # plt.plot(Filter.HPF(Processor.fft_reverse(mag2), fs=fs, cutoff=))
    # plt.show()

if __name__ == "__main__":


    f = 30e6
    fs = f * 100
    duration = 20 / f

    sin, cos = SimpleSinusoidal(f, fs, duration)
    sin2, cos2 = SimpleSinusoidal(f, fs, duration)

    mag1, result1 = Processor.fft(sin)
    mag2, result2 = Processor.fft(cos)


    SignalAnalizeView(sin, duration, fs)



