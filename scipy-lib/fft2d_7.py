import numpy as np

import scipy.datasets as datasets
from scipy import fftpack

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


# načtení matice
ascent = datasets.ascent()

# výpočet 2D FFT
ascent_fft = fftpack.fft2(ascent)

high_freq_limit = 50

ascent_fft[high_freq_limit:512-high_freq_limit] = 0
ascent_fft[:, high_freq_limit:512-high_freq_limit] = 0

ascent_time = fftpack.ifft2(ascent_fft)

# zobrazení výsledku
plt.imshow(ascent_time.real, cmap="gray")

# uložení matice do rastrového obrázku
plt.savefig("fft2d_7.png")

# zobrazení grafu
plt.show()
