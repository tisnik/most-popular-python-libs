from scipy.fft import fft, ifft

import numpy as np

t = np.array([1, 2, 3, 4])

# rychlá Fourierova transformace
f = fft(t)

for x in f:
    print(x)

print("-" * 10)

t2 = ifft(f)

for x in t2:
    print(x)

