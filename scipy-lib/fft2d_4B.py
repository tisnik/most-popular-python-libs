import numpy as np

import scipy.datasets as datasets
from scipy import fftpack
from scipy.fft import fftshift

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


# načtení matice
ascent = datasets.ascent()

# výpočet 2D FFT
ascent_fft = fftpack.fft2(ascent)

# posun ve frekvenční oblasti
ascent_fft = fftshift(ascent_fft)

# zobrazení výsledku
plt.imshow(np.abs(ascent_fft), norm=LogNorm(vmin=5))
plt.colorbar()

plt.title("2D FFT")

# uložení matice do rastrového obrázku
plt.savefig("fft2d_4B.png")

# zobrazení grafu
plt.show()
