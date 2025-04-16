# budeme provádět vykreslování de facto standardní knihovnou Matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_circles

# velikost obrázku s grafem
plt.subplots(figsize=(6.4, 6.4))

# testovací data
n_samples = 2000

samples, labels = make_circles(
    n_samples=n_samples, factor=0.5, noise=0.05
)

# vykreslení bodů v rovině
plt.scatter(samples[:, 0], samples[:, 1], s=1.5, cmap=plt.cm.Set1)

# uložení grafu do souboru
plt.savefig("circles1.png")

# vykreslení na obrazovku
plt.show()
