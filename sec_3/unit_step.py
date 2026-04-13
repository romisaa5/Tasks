import numpy as np
import matplotlib.pyplot as plt
n = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
u_n = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
plt.stem(n, u_n)
plt.title("unit step impulse")
plt.xlabel('N')
plt.ylabel('Amplitude')
plt.show()