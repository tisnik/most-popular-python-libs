#!/usr/bin/env python

#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

# Vykreslení bodů v 3D prostoru

import matplotlib.pyplot as plt

import numpy as np
from sklearn.cluster import KMeans

# počet oblastí, kam se budou data sdružovat
n_components = 8

# počet vygenerovaných bodů
n_samples = 50000

samples = np.random.rand(n_samples, 3)

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
plt.savefig("kmeans_spread_random_3D.png")

# uložení grafu do souboru
ax.view_init(90, -90, 0)
plt.savefig("kmeans_spread_random_view_1.png")

ax.view_init(0, -90, 0)
plt.savefig("kmeans_spread_random_view_2.png")

ax.view_init(0, 0, 0)
plt.savefig("kmeans_spread_random_view_3.png")
