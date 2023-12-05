# budeme provádět vykreslování de facto standardní knihovnou Matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_circles

# testovací data
n_samples = 2000

samples, labels = make_circles(
    n_samples=n_samples, factor=0.5, noise=0.10
)

samples = samples[:, ::-1]

# vykreslení bodů v rovině
plt.scatter(samples[:, 0], samples[:, 1], s=1.0)

# uložení grafu do souboru
plt.savefig("circles2.png")

# vykreslení na obrazovku
plt.show()
