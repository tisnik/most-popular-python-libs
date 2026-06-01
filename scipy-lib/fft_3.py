from scipy.fft import fft

import numpy as np

# signál
t = np.cos(np.linspace(0, 2.0*np.pi, 100))

# rychlá Fourierova transformace
f = fft(t)

for x in f:
    print(x)
