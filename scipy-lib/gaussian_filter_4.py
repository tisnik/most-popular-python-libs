
import matplotlib.pyplot as plt
from scipy import ndimage

original = plt.imread("moonlanding.png").astype(float)

# aplikace filtru
blurred = ndimage.gaussian_filter(original, sigma=0.5)

# zobrazení výsledku
plt.imshow(blurred, cmap="gray")

# uložení matice do rastrového obrázku
plt.savefig("gaussian_filter_4.png")

# zobrazení grafu
plt.show()
