import matplotlib.pyplot as plt
import scipy.datasets as datasets
from scipy import fftpack

import numpy as np

# načtení matice
ascent = datasets.ascent()

# výpočet 2D FFT
ascent_fft = fftpack.fft2(ascent)

# zobrazení výsledku, změna měřítka
plt.imshow(np.abs(np.log10(ascent_fft)))

plt.title("2D FFT")

# uložení matice do rastrového obrázku
plt.savefig("fft2d_3.png")

# zobrazení grafu
plt.show()
