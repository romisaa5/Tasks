import numpy as np
import matplotlib.pyplot as plt
n = np.arange(-5, 6)     
delta = np.zeros_like(n)  
delta[n == 0] = 1        
plt.stem(n, delta)
plt.title("unit impulse")
plt.xlabel('N'); plt.ylabel('Amplitude')
plt.show()