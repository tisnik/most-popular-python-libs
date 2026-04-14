import scipy.datasets as datasets
import matplotlib.pyplot as plt

# načtení matice
raccoon = datasets.face()

# zobrazení matice s volbou barvové palety
plt.imshow(raccoon, cmap="gray")

# uložení matice do rastrového obrázku
plt.savefig("datasets_5.png")

# zobrazení grafu
plt.show()
