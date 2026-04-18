import numpy as np

import matplotlib.pyplot as plt

from scipy.signal import convolve
import scipy.datasets as datasets


# načtení matice
ascent = datasets.ascent()

kernel = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1],
])

print("Kernel:")
print(kernel)

# výpočet konvoluce
filtered = convolve(ascent, kernel)

# zobrazení výsledku
plt.imshow(filtered, cmap="gray")

plt.title("2D convolution")

# uložení grafu s průběhem signálu
plt.savefig("convolve_2d_3.png")

# zobrazení grafu
plt.show()
