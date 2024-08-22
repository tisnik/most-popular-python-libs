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
#
# Tento demonstracni priklad je pouzity v serialu o datove analyze
# s vyuzitim programovaciho jazyka Python:
# https://www.root.cz/serialy/datova-analyza-s-vyuzitim-jazyka-python/
#
# Clanek, kde je tento demonstracni priklad pouzit:
# Datová analýza s využitím nástroje scikit-learn: první kroky
# https://www.root.cz/clanky/datova-analyza-s-vyuzitim-nastroje-scikit-learn-prvni-kroky/
#

import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

# nacteni datove sady
iris = load_iris()

# nacteni datove sady
data = iris.data

# mrizka s diagramy/grafy
fig, axes = plt.subplots(nrows=2, ncols=2)
fig.set_figheight(15)
fig.set_figwidth(15)

plt.figure(1)
colors = ["#4444cc", "#cc4444", "#cccc44", "#44cccc", "#cc44cc"]

# clustering
kmeans = KMeans(n_clusters=3, random_state=0, n_init="auto").fit(data)

def draw_kmeans(col, row, serie1, serie2):
    ax = axes[col][row]

    for i, color in enumerate(colors):
        selector = kmeans.labels_ == i
        ax.scatter(data[selector, serie1], data[selector, serie2], c=color, marker=".", s=50)

    ax.scatter(kmeans.cluster_centers_[:, serie1], kmeans.cluster_centers_[:, serie2], c="red", s=100)
    ax.set(xlabel=iris.feature_names[serie1], ylabel=iris.feature_names[serie2])


draw_kmeans(0, 0, 0, 1)
draw_kmeans(0, 1, 0, 2)
draw_kmeans(1, 0, 1, 2)
draw_kmeans(1, 1, 1, 3)

plt.tight_layout()

# uložení grafu do souboru
plt.savefig("58.png")

# vykreslení na obrazovku
plt.show()
