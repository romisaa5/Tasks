import numpy as np
import matplotlib.pyplot as plt
n = np.arange(-5, 6)
u_n = np.zeros_like(n)
u_n[n >= 0] = 1           # كل اللي >= 0 يبقى 1

plt.stem(n, u_n)
plt.title("unit step")
plt.show()