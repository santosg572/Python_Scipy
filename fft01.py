import scipy as sp 
import numpy as np
import matplotlib.pyplot as plt

Fs = 1000;            # Sampling frequency                    
T = 1/Fs;             # Sampling period       
L = 1500;             # Length of signal
t = np.arange(L)
t = t*T;        # Time vector

S = 0.8 + 0.7*np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t);

X = S + 2*np.random.randn(len(t));

plt.subplot(2,1,1)
plt.plot(1000*t,X)
plt.xlabel("t (milliseconds)")
plt.ylabel("X(t)")

#plt.show()

Y = sp.fft.fft(X)

tt =  np.arange(1,L+1)/L

tt = Fs*tt

plt.subplot(2,1,2)
plt.plot(tt, np.abs(Y))
plt.xlabel("f (Hz)")
plt.ylabel("|fft(X)|")

plt.show()




