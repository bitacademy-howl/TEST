import os
import sys

import matplotlib
import matplotlib.pyplot as plt


sys.path.insert(0, os.path.abspath('./src/'))


def test_detect():
    import numpy as np
    from un0rick_test.tests.Process import Process

    fs = 1000
    f0 = 20
    cycles = 20

    t = np.arange(0, cycles*1/f0, 1/fs)
    carrier = np.sin(2*np.pi*f0*t)
    matplotlib.axes.Axes.plot
    #
    # plt.show()

    modulation = 1-np.power(1/((cycles*1/f0)/2), 2)*np.power(t-(cycles*1/f0)/2, 2)
    raw_signal = np.multiply(carrier, modulation)
    env_signal = Process.detect(raw_signal)

    fig = plt.figure()
    ax1 = fig.add_subplot(3,1, 1)
    ax2 = fig.add_subplot(3,1, 2)
    ax3 = fig.add_subplot(3,1, 3)

    ax1.plot(t, carrier, label=carrier)
    ax1.plot(t, modulation, label=modulation)
    ax2.plot(t, raw_signal)
    ax3.plot(t, env_signal)
    plt.show()


    # calculate rms between modulation function and detected signal
    rms = np.sqrt(np.mean(np.power(np.subtract(env_signal, modulation), 2)))
    assert rms < 0.005

    # test output dimensions for matrix input
    raw_mat = np.array([raw_signal for ii in range(0, 4)])
    env_mat = Process.detect(raw_mat)
    assert np.array_equal(raw_mat.shape, env_mat.shape)

    # test for detection along fastest changing dim
    env_mat_row = np.squeeze(env_mat[2])
    assert np.allclose(env_mat_row, env_signal, rtol=1e-05, atol=1e-08,
                       equal_nan=True)

test_detect()