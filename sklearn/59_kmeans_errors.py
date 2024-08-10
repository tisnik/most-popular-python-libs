#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import matplotlib.pyplot as plt

from sklearn.cluster import SpectralClustering
from sklearn.datasets import load_iris

# nacteni datove sady
iris = load_iris()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = iris.data

targets = iris.target

# clustering
# kmeans = KMeans(n_clusters=3, random_state=0, n_init="auto").fit(data)
kmeans = SpectralClustering(n_clusters=3, eigen_solver="arpack", affinity="nearest_neighbors", random_state=0).fit(data)

# vykresleni mrizky korelacnich diagramu
fig, axes = plt.subplots(nrows=3, ncols=1)
fig.set_figheight(15)
fig.set_figwidth(10)

# korektni druhy z datove sady
ax = axes[0]
scatter = ax.scatter(data[:, 0], data[:, 1], c=iris.target)

colors = ["#4444cc", "#cc4444", "#cccc44"]

# rozdeleni do clusteru provedene algoritmem
ax = axes[1]
for i, color in enumerate(colors):
    selector = kmeans.labels_ == i
    ax.scatter(data[selector, 0], data[selector, 1], c=color)

# vizualizace chybne "predpovedi" clusteringu
ax = axes[2]
colors = []
for i in range(len(targets)):
    t = targets[i]
    k = kmeans.labels_[i]
    color = "#cc4444"
    # cislo clusteru odpovida druhu rostliny
    if t == k:
        color = "#44cc44"
    colors.append(color)
ax.scatter(data[:, 0], data[:, 1], c=colors)

plt.tight_layout()

# uložení grafu do souboru
plt.savefig("59.png")

# vykreslení na obrazovku
plt.show()
