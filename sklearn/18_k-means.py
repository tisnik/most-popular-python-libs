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

# nalézt centra oblastí
centers_init, indices = kmeans_plusplus(samples, n_clusters=6, random_state=0)

plt.scatter(centers_init[:, 0], centers_init[:, 1], c="red", s=50)
plt.title("K-Means++")

# uložení grafu do souboru
plt.savefig(f"k_means_1.png")

# vykreslení na obrazovku
plt.show()
