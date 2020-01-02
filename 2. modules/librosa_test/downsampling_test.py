
import matplotlib.pyplot as plt
import numpy as np
import librosa

sampling_rate = 80 # (UNITS : Mhz)
resampling_rate = 40 # (UNITS : Mhz)

input = [1,2,56,1,76,2,4375,34,567,4,5679,0,659,0,23,45,23,45,0,23,3,475,8,567,9]

data = np.array(input, dtype=np.float)


def down_sampling(input_wave, origin_sr, resample_sr):
    # y, sr = librosa.load(input_wave, sr=origin_sr)
    resample = librosa.resample(input_wave, origin_sr, resample_sr)

    print("original wav sr : {}, orginal wav shape : {}, resample wav sr : {},  resample shape : {}".format(origin_sr, input_wave.shape, resample_sr, resample.shape))
    return resample

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(data)
ax2.plot(down_sampling(data, sampling_rate, resampling_rate))
plt.show()

