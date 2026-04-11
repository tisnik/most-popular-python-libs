import numpy as np

import scipy.datasets as datasets
from scipy.fft import dct

import matplotlib.pyplot as plt


# načtení matice
ascent = datasets.ascent()

# výpočet 2D DCT
ascent_dct = dct(ascent)

# zobrazení výsledku, změna měřítka
plt.imshow(ascent_dct)

plt.title("2D DCT")

# uložení matice do rastrového obrázku
plt.savefig("dct_7.png")

# zobrazení grafu
plt.show()
