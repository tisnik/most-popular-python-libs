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

from sklearn.datasets import fetch_california_housing

# nacteni datove sady
housings = fetch_california_housing()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = housings["data"]

FIRST_DIM = 2
SECOND_DIM = 3

# vykresleni korelacniho diagramu pro dvojici vybranych atributu
# prvni sloupec: x-ove souradnice
# druhy sloupec: y-ove souradnice
plt.scatter(data[:, FIRST_DIM], data[:, SECOND_DIM], c=housings.target, s=2)
plt.title("Classes")

# popisky os
plt.xlabel(housings.feature_names[FIRST_DIM])
plt.ylabel(housings.feature_names[SECOND_DIM])

# ulozeni diagramu do souboru
plt.savefig("76_B.png")

# zobrazeni diagramu
plt.show()
