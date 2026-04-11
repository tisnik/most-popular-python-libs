from scipy.fft import dct

import numpy as np

t = np.array([1, 2, 3, 4])

# diskrétní kosinová transformace
f = dct(t)

for x in f:
    print(x)
