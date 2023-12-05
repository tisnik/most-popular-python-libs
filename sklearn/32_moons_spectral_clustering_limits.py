# budeme provádět vykreslování de facto standardní knihovnou Matplotlib
import matplotlib.pyplot as plt

from sklearn.cluster import SpectralClustering
from sklearn.datasets import make_moons

# testovací data
n_samples = 3000

samples, labels = make_moons(
    n_samples=n_samples, noise=0.15
)

samples = samples[:, ::-1]

plt.figure(1)
colors = ["#4444cc", "#44bb44", "#cc4444", "#cccc44", "#44cccc", "#cc44cc"]

# clustering
spectral = SpectralClustering(n_clusters=2, eigen_solver="arpack", affinity="nearest_neighbors", random_state=0).fit(samples)

# vykreslení bodů s jejich přiřazením ke clusteru
for i, color in enumerate(colors):
    selector = spectral.labels_ == i
    plt.scatter(samples[selector, 0], samples[selector, 1], c=color, marker=".", s=1)

plt.title("Spectral clustering")

# uložení grafu do souboru
plt.savefig("moons_spectral.png")

# vykreslení na obrazovku
plt.show()
