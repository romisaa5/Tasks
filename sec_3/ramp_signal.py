import numpy as np
import matplotlib.pyplot as plt
n = np.arange(-5, 6)
r_n = np.maximum(0, n)
r_n = np.zeros_like(n)
r_n[n >= 0] = n[n >= 0] 
plt.stem(n, r_n)
plt.title("ramp")
plt.show()