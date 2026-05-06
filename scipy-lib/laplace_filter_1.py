import numpy as np

import scipy.datasets as datasets
from scipy import ndimage

import matplotlib.pyplot as plt


# načtení matice
ascent = datasets.ascent()

# aplikace filtru
filtered = ndimage.laplace(ascent)

# zobrazení výsledku, změna měřítka
plt.imshow(filtered, cmap="gray")

plt.title("Laplace filter")

# uložení matice do rastrového obrázku
plt.savefig("laplace_filter_1.png")

# zobrazení grafu
plt.show()
