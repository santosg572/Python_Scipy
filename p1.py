#  https://docs.scipy.org/doc/scipy/reference/generated/scipy.fft.fft.html#scipy.fft.fft

from scipy.fft import fft, fftfreq, fftshift
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(256)

sp = fftshift(fft(np.sin(t)))

freq = fftshift(fftfreq(t.shape[-1]))

plt.plot(freq, sp.real, freq, sp.imag)

plt.show()

