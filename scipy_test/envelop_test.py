import logging
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp, hilbert2

from VO.DDD import DDD_File
from scipy_test.module import FilteredSignal


def envelope(data, bias = 0, axis=-1):
    """
    perform envelope detection on input data by calculating the magnitude of
    the analytic signal

    :param data: input data to envelope detect
    :param axis: dimension along which detection is performed, default: -1
    :return: env_data (np.array)
    """
    data = np.array(data)
    data -= bias
    analytic_data = hilbert(data, N=None, axis=axis)
    # analytic_data = hilbert2(data, N=None)
    amplitude_envelope = np.abs(analytic_data)
    # env_data = np.abs(analytic_data)
    # env_data = np.absolute(analytic_data)

    # instantaneous_phase = np.unwrap(np.angle(analytic_data))
    # instantaneous_frequency = (np.diff(instantaneous_phase) / (2.0 * np.pi) * fs)

    msg = '[detect] Envelope detection finished.'
    print(msg)
    logging.debug(msg)

    return amplitude_envelope

def proc_test_data():

    from VO.DDD import DDD_File

    ddd1 = DDD_File(path="./data/20191204original.ddd")
    ddd1.Load()

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    signal1 = ddd1.GetData()[0:ddd1.GetHeader().GetDepth()]
    signal2 = envelope(signal1, bias=50)

    ax1.plot(signal1)
    ax2.plot(signal2)

    plt.show()

def get_data():
    ddd = DDD_File(path="./data/20191204original.ddd")
    ddd.Load()
    signal = np.array(ddd.GetData()[0:ddd.GetHeader().GetDepth()]) / 255
    return signal


def example():
    duration = 1.0
    # duration = 6.5

    fs = 400.0
    # fs = 80

    null_signal = np.zeros(400)
    print(null_signal.shape)

    samples = int(fs*duration)

    t = np.arange(samples) / fs
    t2 = np.arange(samples*2) / fs

    signal1 = chirp(t, 20.0, t[-1], 100.0) # fundamental freq = 20
    signal2 = signal1 * (1.0 + 0.5 * np.sin(2.0*np.pi*3.0*t) )

    analytic_signal = hilbert(signal2, N=None)
    amplitude_envelope = np.abs(analytic_signal)
    # amplitude_envelope_not_abs = analytic_signal

    signal3 = list(signal2)
    signal3.extend(list(null_signal))
    print(len(signal3))
    signal3 = np.array(signal3)
    analytic_signal3 = hilbert(signal3, N=None)
    amplitude_envelope3 = np.abs(analytic_signal3)

    t4 = np.arange(samples * 2) / fs
    sigseg = list(np.arange(samples / 2) / (fs/2))
    sigseg.extend(sigseg)
    sigseg.extend(sigseg)
    signal4 = sigseg
    analytic_signal4 = hilbert(signal4, N=None)
    amplitude_envelope4 = np.abs(analytic_signal4)


    signal5 = get_data()
    t5 = np.arange(len(signal5))/255

    filteredSignal = FilteredSignal(signal5, fs, cutoff=30)

    analytic_signal5 = hilbert(signal5, N=None)
    amplitude_envelope5 = np.abs(analytic_signal5)


    # instantaneous_phase = np.unwrap(np.angle(analytic_signal))
    # instantaneous_frequency = (np.diff(instantaneous_phase) / (2.0*np.pi) * fs)

    fig = plt.figure()

    ax1 = fig.add_subplot(611)
    ax1.plot(t, label='signal')
    ax1.set_xlabel("time in seconds")
    ax1.legend()

    ax2 = fig.add_subplot(612)
    ax2.plot(t, signal2, label='signal')
    ax2.plot(t, amplitude_envelope, label='envelope')
    ax2.plot(t, analytic_signal, label="not_abs")
    ax2.set_xlabel("time in seconds")
    ax2.legend()

    ax3 = fig.add_subplot(613)
    ax3.plot(t, signal1, label='signal')
    ax3.set_xlabel("time in seconds")
    ax3.legend()

    ax4 = fig.add_subplot(614)
    ax4.plot(t2, signal3, label='signal')
    ax4.plot(t2, amplitude_envelope3, label='envelope')
    ax4.set_xlabel("time in seconds")
    ax4.legend()

    ax5 = fig.add_subplot(615)
    ax5.plot(t4, signal4, label='signal')
    ax5.plot(t4, amplitude_envelope4, label='envelope')
    ax5.set_xlabel("time in seconds")
    ax5.legend()

    ax6 = fig.add_subplot(616)
    ax6.plot(t5, signal5, label='signal')
    ax6.plot(t5, amplitude_envelope5, label='envelope')
    ax6.set_xlabel("time in seconds")
    ax6.legend()
    # ax2 = fig.add_subplot(313)
    # ax2.plot(t[1:], instantaneous_frequency)
    # ax2.set_xlabel("time in seconds")
    # ax2.set_ylim(0.0, 120.0)

    plt.show()

example()
# proc_test_data()
