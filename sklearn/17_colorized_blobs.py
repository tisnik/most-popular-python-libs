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

# vykreslení bodů v rovině s jejich obarvením na základě labelu
plt.figure(1)
colors = ["#4444cc", "#44bb44", "#cc4444", "#cccc44", "#44cccc", "#cc44cc"]

for i, color in enumerate(colors):
    selector = labels == i
    plt.scatter(samples[selector, 0], samples[selector, 1], c=color, marker=".", s=10)

# uložení grafu do souboru
plt.savefig("scatter_3.png")

# vykreslení na obrazovku
plt.show()
