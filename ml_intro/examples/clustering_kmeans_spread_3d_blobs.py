# Vykreslení bodů v 3D prostoru

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# celkový počet vypočtených bodů
n_samples = 10000

# počet oblastí, kam se budou data sdružovat
n_components = 8

samples, _ = make_blobs(
    n_samples=n_samples, n_features=3, centers=n_components,
    cluster_std=1.80, random_state=0
)

# barvy použité pro obarvení bodů
colors = ["#4444cc", "#44bb44", "#cc4444", "#cccc44", "#44cccc", "#cc44cc", "#cccccc", "#000000"]

# příprava 3D grafu
fig = plt.figure(figsize=(6.4, 6.4))
ax = fig.add_subplot(projection="3d")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# clustering
kmeans = KMeans(n_clusters=n_components, random_state=0, n_init="auto").fit(samples)

# vykreslit centra nalezených oblastí
ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], kmeans.cluster_centers_[:, 2], c="red", s=50)

# vykreslení bodů s jejich přiřazením ke clusteru
for i, color in enumerate(colors):
    selector = kmeans.labels_ == i
    ax.scatter(samples[selector,0], samples[selector,1], samples[selector,2], marker=".", s=1)

# uložení grafu do souboru
plt.savefig("kmeans_spread_blobs_3D.png")

# uložení grafu do souboru
ax.view_init(90, -90, 0)
plt.savefig("kmeans_spread_blobs_view_1.png")

ax.view_init(0, -90, 0)
plt.savefig("kmeans_spread_blobs_view_2.png")

ax.view_init(0, 0, 0)
plt.savefig("kmeans_spread_blobs_view_3.png")
