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

# příprava 3D grafu
fig = plt.figure(figsize=(6.4, 6.4))
ax = fig.add_subplot(projection="3d")

# vykreslení grafu
ax.scatter(samples[:,0], samples[:,1], samples[:,2], marker=".", s=1)

# uložení grafu do souboru
plt.savefig("blobs_3D.png")

# zobrazení grafu
plt.show()
