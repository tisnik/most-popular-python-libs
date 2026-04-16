import numpy as np

import scipy.datasets as datasets
from scipy.fft import dst

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


# načtení matice
ascent = datasets.ascent()

# výpočet 2D dst
ascent_dst = dst(ascent)

# zobrazení výsledku, změna měřítka
plt.imshow(ascent_dst, norm=LogNorm(vmin=5))

plt.title("2D dst")

# uložení matice do rastrového obrázku
plt.savefig("dst_2.png")

# zobrazení grafu
plt.show()
