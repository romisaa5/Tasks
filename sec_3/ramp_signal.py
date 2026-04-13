import numpy as np
import matplotlib.pyplot as plt
n = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
r_n = [0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
plt.stem(n, r_n)
plt.title("ramp impulse")
plt.xlabel('N')
plt.ylabel('Amplitude')
plt.show()