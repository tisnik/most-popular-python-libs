from scipy.fft import dct, idct

import numpy as np

t = np.array([1, 2, 3, 4])

f = dct(t)

for x in f:
    print(x)

print("-" * 10)

t2 = idct(f)

for x in t2:
    print(x)

