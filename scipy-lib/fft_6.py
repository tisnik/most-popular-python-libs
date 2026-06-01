from scipy.fft import fft, fftshift

import numpy as np
import matplotlib.pyplot as plt

# signál
t = np.cos(np.linspace(0, 2.0*np.pi, 100))

# rychlá Fourierova transformace
f = fft(t)

f2 = fftshift(f)

# vykreslení výsledného signálu
plt.plot(f2)

# uložení grafu s průběhem signálu
plt.savefig("fft_6.png")
