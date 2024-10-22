import numpy as np
from scipy.fftpack import fft, fftfreq
import matplotlib.pyplot as plt

x = np.arange(0, 10, .1)

y1 = np.sin(2*np.pi*x)
y2 = 2*np.sin(2*np.pi*x/2)
y3 = 3*np.sin(2*np.pi*x/3)

yt = y1+y2+y3

'''
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
'''


Y3 = fft(yt) / (10 * n2) # Transformada normalizada
frq3 = fftfreq(10 * n2, dt2)
fig = plt.figure(figsize=(6, 8))
ax1 = fig.add_subplot(211)
ax1.plot(t3, y3)
ax1.set_xlabel('Tiempo (s)')
ax1.set_ylabel('$y_3(t)$')
ax2 = fig.add_subplot(212)
ax2.vlines(frq3, 0, Y3.imag)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Im($Y_3$)')

plt.show()
