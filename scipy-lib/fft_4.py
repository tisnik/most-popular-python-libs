from scipy.fft import fft

import numpy as np
import matplotlib.pyplot as plt

# signál
t = np.cos(np.linspace(0, 2.0*np.pi, 100))

# rychlá Fourierova transformace
f = fft(t)

# vykreslení výsledného signálu
plt.plot(f)

# uložení grafu s průběhem signálu
plt.savefig("fft_4.png")
