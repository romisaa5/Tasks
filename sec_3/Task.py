import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5, 6)
u_n = np.zeros_like(n)
u_n[n >= 0] = 1
r_n = n * (n >= 0)

plt.plot(n, u_n, drawstyle='steps-post', label='Unit Step')
plt.plot(n, r_n, label='Ramp')

plt.title("Unit Step & Ramp Signal")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.show()