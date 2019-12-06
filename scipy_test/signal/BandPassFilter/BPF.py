import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

# Band Pass Filter in Continuous Time
f_peak = 500
w0_peak = 2*np.pi*f_peak
bandWidth = 200
Q = f_peak/bandWidth
H = 1/w0_peak
H0 = H/Q

num = np.array([H0*w0_peak**2, 0])
den = np.array([1, w0_peak/Q, w0_peak**2])

w, h = sig.freqs(num, den, worN=np.logspace(0, 5, 1000))

plt.figure(figsize=(12,5))
plt.semilogx(toHz(w), 20 * np.log10(abs(h)))
plt.axvline(f_peak, color='k', lw=2)
plt.axvline(f_peak-bandWidth/2, color='k', lw=1)
plt.axvline(f_peak+bandWidth/2, color='k', lw=1)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude response [dB]')
tmpTitle = 'Band Pass Filter, Peak freq. at ' + str(f_peak) + 'Hz in continuous'
plt.title(tmpTitle)
plt.xlim((f_peak-bandWidth/2)*0.1, (f_peak+bandWidth/2)*10)
plt.grid()
plt.show()