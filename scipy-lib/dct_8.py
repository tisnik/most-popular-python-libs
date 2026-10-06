
import matplotlib.pyplot as plt
import scipy.datasets as datasets
from matplotlib.colors import LogNorm
from scipy.fft import dct

# načtení matice
ascent = datasets.ascent()

# výpočet 2D DCT
ascent_dct = dct(ascent)

# zobrazení výsledku, změna měřítka
plt.imshow(ascent_dct, norm=LogNorm(vmin=5))

plt.title("2D DCT")

# uložení matice do rastrového obrázku
plt.savefig("dct_8.png")

# zobrazení grafu
plt.show()
