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

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# nacteni datove sady
iris = load_iris()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = iris.data

# Principal component analysis
reduced = PCA(n_components=3).fit_transform(data)

# vykresleni korelacniho grafu ve 3D
fig = plt.figure(1)
ax = fig.add_subplot(111, projection="3d", elev=-150, azim=110)

ax.scatter(
    reduced[:, 0],
    reduced[:, 1],
    reduced[:, 2],
    c=iris.target,
    s=40,
)


# zbavit se prazdneho mista okolo bunek mrizky
plt.tight_layout()

# ulozeni grafu do souboru
plt.savefig("56.png")

# zobrazeni grafu
plt.show()
