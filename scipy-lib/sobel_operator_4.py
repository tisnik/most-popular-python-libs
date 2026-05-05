import numpy as np

import scipy.datasets as datasets
from scipy import ndimage

import matplotlib.pyplot as plt


# načtení matice
ascent = datasets.ascent()

# aplikace filtru
filtered = ndimage.sobel(ascent, axis=1)

# zobrazení výsledku, změna měřítka
plt.imshow(ascent - filtered, cmap="gray")

plt.title("Sobel operator")

# uložení matice do rastrového obrázku
plt.savefig("sobel_operator_4.png")

# zobrazení grafu
plt.show()
