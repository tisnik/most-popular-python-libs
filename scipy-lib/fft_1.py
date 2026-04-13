from scipy.fft import fft

import numpy as np

t = np.array([1, 2, 3, 4])

# rychlá Fourierova transformace
f = fft(t)

for x in f:
    print(x)
