import numpy as np
import matplotlib.pyplot as plt
n = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
delta = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
plt.stem(n, delta)
plt.title("unit impulse")
plt.xlabel('N')
plt.ylabel('Amplitude')
plt.show()