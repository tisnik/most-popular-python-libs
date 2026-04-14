import scipy.datasets as datasets
import matplotlib.pyplot as plt

# načtení matice
ascent = datasets.ascent()

# zobrazení matice
plt.imshow(ascent)

# uložení matice do rastrového obrázku
plt.savefig("datasets_2.png")

# zobrazení grafu
plt.show()
