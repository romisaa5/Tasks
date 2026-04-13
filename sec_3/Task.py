import numpy as np
import matplotlib.pyplot as plt
n = np.arange(-5, 6)
u_n = np.zeros_like(n); u_n[n >= 0] = 1
r_n = np.maximum(0, n)
plt.subplot(1, 2, 1)
plt.plot(n, u_n, drawstyle='steps-post', color='blue', linewidth=2)
plt.title("unit step")
plt.grid(True)
plt.subplot(1, 2, 2)
plt.plot(n, r_n, color='red', linewidth=2)
plt.title("ramp")
plt.grid(True)

plt.show()