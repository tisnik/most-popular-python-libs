import matplotlib.pyplot as plt
import scipy.datasets as datasets
from matplotlib.colors import LogNorm
from scipy import fftpack

import numpy as np

# načtení matice
ascent = datasets.ascent()

# výpočet 2D FFT
ascent_fft = fftpack.fft2(ascent)

# zobrazení výsledku
plt.imshow(np.abs(ascent_fft), norm=LogNorm(vmin=5))
plt.colorbar()

plt.title("2D FFT")

# uložení matice do rastrového obrázku
plt.savefig("fft2d_4.png")

# zobrazení grafu
plt.show()
