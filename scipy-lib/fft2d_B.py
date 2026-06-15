import numpy as np

import scipy.datasets as datasets
from scipy import fftpack

import matplotlib.pyplot as plt

original = plt.imread("moonlanding.png").astype(float)

# výpočet 2D FFT
original_fft = fftpack.fft2(original)

high_freq_limit = 100
r, c = original_fft.shape

original_fft[high_freq_limit:r-high_freq_limit] = 0
original_fft[:, high_freq_limit:c-high_freq_limit] = 0

filtered = fftpack.ifft2(original_fft)

# zobrazení výsledku
plt.imshow(filtered.real, cmap="gray")

# uložení matice do rastrového obrázku
plt.savefig("fft2d_B.png")

# zobrazení grafu
plt.show()
