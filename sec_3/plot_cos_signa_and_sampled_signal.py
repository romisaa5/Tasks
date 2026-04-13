import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 1, 0.001)  
xt = np.sin(2 * np.pi * 3 * t)

plt.plot(t, xt)
plt.title('sin wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()
n=np.arange(0,1,0.01)
xn=np.sin(2*np.pi*3*n)
plt.stem(n,xn)
plt.title('sampled sin wave')
plt.xlabel('n')
plt.ylabel('amplitude')
plt.show()