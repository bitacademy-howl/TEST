import logging
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp, hilbert2, butter, filtfilt

from VO.DDD import DDD_File

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


def FilteredSignal(signal, fs, cutoff):
    B, A = butter(1, cutoff / (fs / 2), btype="low")
    filtered_signal = filtfilt(B, A, signal, axis=0)
    return filtered_signal
