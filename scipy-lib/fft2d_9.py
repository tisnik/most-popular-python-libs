import numpy as np

import scipy.datasets as datasets
import matplotlib.pyplot as plt

# načtení matice
ascent = datasets.ascent()

# vygenerování šumu
noise = np.random.normal(0, 60, ascent.shape)

# zašumění obrázku
ascent = ascent + noise

# zobrazení matice
plt.imshow(ascent, cmap="gray")

# uložení matice do rastrového obrázku
plt.savefig("fft2d_9.png")

# zobrazení grafu
plt.show()
