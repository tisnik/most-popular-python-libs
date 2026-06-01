from scipy.fft import fft

import numpy as np
import matplotlib.pyplot as plt

# signál
t = np.cos(np.linspace(0, 2.0*np.pi, 100))

# rychlá Fourierova transformace
f = fft(t)[1:len(t)//2]

# vykreslení výsledného signálu
plt.plot(f)

# uložení grafu s průběhem signálu
plt.savefig("fft_5.png")
