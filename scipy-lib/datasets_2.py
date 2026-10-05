import matplotlib.pyplot as plt
import scipy.datasets as datasets

# načtení matice
ascent = datasets.ascent()

# zobrazení matice
plt.imshow(ascent)

# uložení matice do rastrového obrázku
plt.savefig("datasets_2.png")

# zobrazení grafu
plt.show()
