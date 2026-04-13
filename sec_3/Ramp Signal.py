import numpy as np
import matplotlib.pyplot as plt
n = np.arange(-5, 6)

# طريقة 1: باستخدام maximum
r_n = np.maximum(0, n)

# طريقة 2: باستخدام zeros_like
r_n = np.zeros_like(n)
r_n[n >= 0] = n[n >= 0]  # قيمة n نفسها

plt.stem(n, r_n)
plt.title("ramp")
plt.show()