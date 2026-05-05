import numpy as np

import scipy.datasets as datasets
from scipy import ndimage

import matplotlib.pyplot as plt


# načtení matice
ascent = datasets.ascent()

# aplikace filtru
filtered = ndimage.sobel(ascent, axis=0)

# zobrazení výsledku, změna měřítka
plt.imshow(ascent - filtered, cmap="gray")

plt.title("Sobel operator")

# uložení matice do rastrového obrázku
plt.savefig("sobel_operator_3.png")

# zobrazení grafu
plt.show()
