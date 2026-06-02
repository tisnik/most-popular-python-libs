import scipy.signal as signal
from scipy.fft import fft, fftshift

import numpy as np
import matplotlib.pyplot as plt

# filtr
win = signal.windows.hann(50)

# rychlá Fourierova transformace
f = fft(win, 1024) / (len(win)/2.0)

# rozsah normalizovaných frekvencí na x-ové ose
freq = np.linspace(-0.5, 0.5, len(f))

response = np.abs(fftshift(f / abs(f).max()))

# vykreslení výsledného signálu
plt.plot(freq, response)

# uložení grafu s průběhem signálu
plt.savefig("fft_7.png")

# zobrazení grafu
plt.show()
