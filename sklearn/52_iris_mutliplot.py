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

from sklearn.datasets import load_iris

# nacteni datove sady
iris = load_iris()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = iris.data

# vykresleni mrizky korelacnich diagramu
fig, axes = plt.subplots(nrows=4, ncols=4)

# rozmery vysledneho obrazku
fig.set_figheight(15)
fig.set_figwidth(15)

# vyplneni mrizky
for row in range(4):
    for column in range(4):
        ax = axes[row][column]
        if row == column:
            # na diagonale jsou prazdna mista
            fig.delaxes(ax)
            continue
        # pridat korelacni diagram do mrizky
        # sloupec row: x-ove souradnice
        # sloupec column: y-ove souradnice
        scatter = ax.scatter(data[:, row], data[:, column], c=iris.target)
        # popisky os
        ax.set(xlabel=iris.feature_names[row], ylabel=iris.feature_names[column])


# zbavit se prazdneho mista okolo bunek mrizky
plt.tight_layout()

# ulozeni diagramu do souboru
plt.savefig("52.png")

# zobrazeni diagramu
plt.show()
