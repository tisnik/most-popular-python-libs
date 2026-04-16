import numpy as np

import scipy.datasets as datasets
from scipy import fftpack
from scipy.fft import fftshift

import matplotlib.pyplot as plt


# načtení matice
ascent = datasets.ascent()

# výpočet 2D FFT
ascent_fft = fftpack.fft2(ascent)

# posun ve frekvenční oblasti
ascent_fft = fftshift(ascent_fft)

# zobrazení výsledku, změna měřítka
plt.imshow(np.abs(np.log10(ascent_fft)))

plt.title("2D FFT")

# uložení matice do rastrového obrázku
plt.savefig("fft2d_3B.png")

# zobrazení grafu
plt.show()
