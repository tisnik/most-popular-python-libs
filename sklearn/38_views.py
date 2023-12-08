#!/usr/bin/env python

# Vykreslení bodů v 3D prostoru

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs


# celkový počet vypočtených bodů
n_samples = 10000

# počet oblastí, kam se budou data sdružovat
n_components = 8

samples, labels = make_blobs(
    n_samples=n_samples, n_features=3, centers=n_components,
    cluster_std=1.20, random_state=0
)

# příprava 3D grafu
fig = plt.figure(figsize=(6.4, 6.4))
ax = fig.add_subplot(projection="3d")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# vykreslení grafu
ax.scatter(samples[:,0], samples[:,1], samples[:,2], marker=".", s=1)

# uložení grafu do souboru
ax.view_init(90, -90, 0)
plt.savefig("blobs_view_1.png")

ax.view_init(0, -90, 0)
plt.savefig("blobs_view_2.png")

ax.view_init(0, 0, 0)
plt.savefig("blobs_view_3.png")
