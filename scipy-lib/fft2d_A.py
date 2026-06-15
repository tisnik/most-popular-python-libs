import numpy as np

import scipy.datasets as datasets
from scipy import fftpack

import matplotlib.pyplot as plt


# načtení matice
ascent = datasets.ascent()

# vygenerování šumu
noise = np.random.normal(0, 60, ascent.shape)

# zašumění obrázku
ascent = ascent + noise

# výpočet 2D FFT
ascent_fft = fftpack.fft2(ascent)

high_freq_limit = 100

ascent_fft[high_freq_limit:512-high_freq_limit] = 0
ascent_fft[:, high_freq_limit:512-high_freq_limit] = 0

ascent_time = fftpack.ifft2(ascent_fft)

# zobrazení výsledku
plt.imshow(ascent_time.real, cmap="gray")

# uložení matice do rastrového obrázku
plt.savefig("fft2d_A.png")

# zobrazení grafu
plt.show()
