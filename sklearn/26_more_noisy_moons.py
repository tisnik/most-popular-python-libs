# budeme provádět vykreslování de facto standardní knihovnou Matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_moons

# testovací data
n_samples = 2000

samples, labels = make_moons(
    n_samples=n_samples, noise=0.15
)

samples = samples[:, ::-1]

# vykreslení bodů v rovině
plt.scatter(samples[:, 0], samples[:, 1], s=1.0)

# uložení grafu do souboru
plt.savefig("moons2.png")

# vykreslení na obrazovku
plt.show()
