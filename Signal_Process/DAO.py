from scipy.signal import chirp, hilbert

from VO.DDD_python_3x import DDD_File
import numpy as np

def GetData():
    ddd = DDD_File(path="./data/20191204original.ddd")
    ddd.Load()
    signal = np.array(ddd.GetData()[0:ddd.GetHeader().GetDepth()])
    return signal

def GetSimpleSignal():
    duration = 10.0
    # duration = 6.5

    fs = 400.0
    # fs = 80

    null_signal = np.zeros(400)
    print(null_signal.shape)

    samples = int(fs*duration)

    t = np.arange(samples) / fs
    t2 = np.arange(samples*2) / fs

    signal1 = chirp(t, 20.0, t[-1], 100.0) # fundamental freq = 20
    signal2 = signal1 * (1.0 + 0.5 * np.sin(2.0*np.pi*3.0*t))

    return signal1, signal2, t

