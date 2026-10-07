
import matplotlib.pyplot as plt
import scipy.datasets as datasets
from matplotlib.colors import LogNorm
from scipy.fft import dst

# načtení matice
ascent = datasets.ascent()

# výpočet 2D dst
ascent_dst = dst(ascent)

# zobrazení výsledku, změna měřítka
plt.imshow(ascent_dst, norm=LogNorm(vmin=5))

plt.title("2D dst")

# uložení matice do rastrového obrázku
plt.savefig("dst_2.png")

# zobrazení grafu
plt.show()
