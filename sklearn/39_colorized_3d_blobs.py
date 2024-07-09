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

from sklearn.datasets import make_blobs

# celkový počet vypočtených bodů
n_samples = 10000

# počet oblastí, kam se budou data sdružovat
n_components = 8

samples, labels = make_blobs(
    n_samples=n_samples, n_features=3, centers=n_components,
    cluster_std=0.80, random_state=0
)

# barvy použité pro obarvení bodů
colors = ["#4444cc", "#44bb44", "#cc4444", "#cccc44", "#44cccc", "#cc44cc", "#cccccc", "#000000"]

# příprava 3D grafu
fig = plt.figure(figsize=(6.4, 6.4))
ax = fig.add_subplot(projection="3d")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# vykreslení grafu
for i, color in enumerate(colors):
    selector = labels == i
    ax.scatter(samples[selector,0], samples[selector,1], samples[selector,2], marker=".", s=1)

# uložení grafu do souboru
plt.savefig("colorized_blobs_3D.png")

# uložení grafu do souboru
ax.view_init(90, -90, 0)
plt.savefig("colorized_blobs_view_1.png")

ax.view_init(0, -90, 0)
plt.savefig("colorized_blobs_view_2.png")

ax.view_init(0, 0, 0)
plt.savefig("colorized_blobs_view_3.png")
