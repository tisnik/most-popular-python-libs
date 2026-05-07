import numpy as np

import scipy.datasets as datasets
from scipy import ndimage

import matplotlib.pyplot as plt


# načtení matice
ascent = datasets.ascent()

# aplikace filtru
blurred = ndimage.gaussian_filter(ascent, sigma=5.0)

# zobrazení výsledku, změna měřítka
plt.imshow(blurred, cmap="gray")

plt.title("Gaussian filter")

# uložení matice do rastrového obrázku
plt.savefig("gaussian_filter_2.png")

# zobrazení grafu
plt.show()
