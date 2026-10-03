import matplotlib.pyplot as plt
import scipy.datasets as datasets
from scipy.signal import convolve

import numpy as np

# načtení matice
ascent = datasets.ascent()

kernel = np.array([
    [ 1, 2, 1 ],
    [ 2, 4, 2 ],
    [ 1, 2, 1 ],
])

print("Kernel:")
print(kernel)

# výpočet konvoluce
filtered = convolve(ascent, kernel)

# zobrazení výsledku
plt.imshow(filtered, cmap="gray")

plt.title("2D convolution")

# uložení grafu s průběhem signálu
plt.savefig("convolve_2d_2.png")

# zobrazení grafu
plt.show()
