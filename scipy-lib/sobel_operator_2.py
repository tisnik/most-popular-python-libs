
import matplotlib.pyplot as plt
import scipy.datasets as datasets
from scipy import ndimage

# načtení matice
ascent = datasets.ascent()

# aplikace filtru
filtered = ndimage.sobel(ascent, axis=1)

# zobrazení výsledku, změna měřítka
plt.imshow(filtered, cmap="gray")

plt.title("Sobel operator")

# uložení matice do rastrového obrázku
plt.savefig("sobel_operator_2.png")

# zobrazení grafu
plt.show()
