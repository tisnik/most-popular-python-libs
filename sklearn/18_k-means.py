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

# budeme provádět vykreslování de facto standardní knihovnou Matplotlib
import matplotlib.pyplot as plt

# funkce s implementací algoritmu pro clustering
from sklearn.cluster import kmeans_plusplus

# import funkce, která dokáže vygenerovat množinu bodů v rovině sdružených do oblastí
from sklearn.datasets import make_blobs

# testovací data
n_samples = 1000

# počet oblastí, kam se budou data sdružovat
n_components = 6

# vygenerovat množinu bodů v rovině sdružených do oblastí
samples, labels = make_blobs(
    n_samples=n_samples, centers=n_components, cluster_std=0.60, random_state=0
)

samples = samples[:, ::-1]

# nalézt centra oblastí
centers_init, indices = kmeans_plusplus(samples, n_clusters=6, random_state=0)

plt.scatter(centers_init[:, 0], centers_init[:, 1], c="red", s=50)
plt.title("K-Means++")

# uložení grafu do souboru
plt.savefig("k_means_1.png")

# vykreslení na obrazovku
plt.show()
