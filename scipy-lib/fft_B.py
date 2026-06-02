import scipy.signal as signal
from scipy.fft import fft, fftshift

import numpy as np
import matplotlib.pyplot as plt

# signal
t = np.zeros(50) + np.ones(50) + np.zeros(50)

# rychlá Fourierova transformace
f = fft(t, 1024) / (len(t)/2.0)

# rozsah normalizovaných frekvencí na x-ové ose
freq = np.linspace(-0.5, 0.5, len(f))

response = np.abs(fftshift(f / abs(f).max()))

# vykreslení výsledného signálu
plt.plot(freq, response)

# uložení grafu s průběhem signálu
plt.savefig("fft_B.png")

# zobrazení grafu
plt.show()
