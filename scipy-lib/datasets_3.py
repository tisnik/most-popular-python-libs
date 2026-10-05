import matplotlib.pyplot as plt
import scipy.datasets as datasets

# načtení matice
ascent = datasets.ascent()

# zobrazení matice s volbou barvové palety
plt.imshow(ascent, cmap="gray")

# uložení matice do rastrového obrázku
plt.savefig("datasets_3.png")

# zobrazení grafu
plt.show()
