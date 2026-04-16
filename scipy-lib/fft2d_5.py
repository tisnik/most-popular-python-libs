import numpy as np

import scipy.datasets as datasets
from scipy import fftpack

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


# načtení matice
ascent = datasets.ascent()

# výpočet 2D FFT
ascent_fft = fftpack.fft2(ascent)

ascent_time = fftpack.ifft2(ascent_fft)

# zobrazení výsledku
plt.imshow(np.abs(ascent_time), cmap="gray")

# uložení matice do rastrového obrázku
plt.savefig("fft2d_5.png")

# zobrazení grafu
plt.show()
