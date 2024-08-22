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

# nacteni datove sady
iris = load_iris()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = iris.data

# vykresleni korelacniho diagramu pro dvojici vybranych atributu
_, ax = plt.subplots()

# prvni sloupec: x-ove souradnice
# druhy sloupec: y-ove souradnice
scatter = ax.scatter(data[:, 0], data[:, 1], c=iris.target)

# popisky os
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])

# pridani legendy do diagramu
ax.legend(scatter.legend_elements()[0], iris.target_names, loc="upper right", title="Classes")

# ulozeni diagramu do souboru
plt.savefig("51.png")

# zobrazeni diagramu
plt.show()
