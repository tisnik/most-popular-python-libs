# budeme provádět vykreslování de facto standardní knihovnou Matplotlib
import matplotlib.pyplot as plt

from sklearn.cluster import kmeans_plusplus
from sklearn.datasets import make_blobs

# testovací data
n_samples = 1000

# počet oblastí, kam se budou data sdružovat
n_components = 6

samples, labels = make_blobs(
    n_samples=n_samples, centers=n_components, cluster_std=0.60, random_state=0
)

samples = samples[:, ::-1]

# vykreslení bodů v rovině
plt.scatter(samples[:, 0], samples[:, 1], marker=".", s=10)

# uložení grafu do souboru
plt.savefig(f"scatter_2.png")

# vykreslení na obrazovku
plt.show()
