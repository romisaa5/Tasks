import numpy as np
import matplotlib.pyplot as plt
n = np.arange(-5, 6)       # من -5 لـ 5
delta = np.zeros_like(n)   # كل الأصفار
delta[n == 0] = 1         # 1 عند الصفر بس

plt.stem(n, delta)
plt.title("unit impulse")
plt.xlabel('N'); plt.ylabel('Amplitude')
plt.show()