
import matplotlib.pyplot as plt
import scipy.datasets as datasets
from matplotlib.colors import LogNorm
from scipy import ndimage
from scipy.fft import dct

# načtení matice
ascent = datasets.ascent()

blurred = ndimage.gaussian_filter(ascent, sigma=2.0)

# výpočet 2D DCT
blurred_dct = dct(blurred)

# zobrazení výsledku, změna měřítka
plt.imshow(blurred_dct, norm=LogNorm(vmin=5))

plt.title("2D DCT")

# uložení matice do rastrového obrázku
plt.savefig("dct_8B.png")

# zobrazení grafu
plt.show()
