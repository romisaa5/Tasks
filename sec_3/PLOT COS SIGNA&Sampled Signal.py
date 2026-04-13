import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 1, 0.001)  # محور الزمن

# sin بتردد 3 Hz
xt = np.sin(2 * np.pi * 3 * t)

plt.plot(t, xt)
plt.title('sin wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()
 # sampled
n=np.arange(0,1,0.01)
xn=np.sin(2*np.pi*3*n)
# to plot the signal : stem: plot discrete signal
plt.stem(n,xn)
plt.title('sampled sin wave')
plt.xlabel('n')
plt.ylabel('amplitude')
plt.show()