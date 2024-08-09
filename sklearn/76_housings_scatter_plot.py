import matplotlib.pyplot as plt

from sklearn.datasets import fetch_california_housing

# nacteni datove sady
housings = fetch_california_housing()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = housings["data"]


# vykresleni korelacniho diagramu pro dvojici vybranych atributu
# prvni sloupec: x-ove souradnice
# druhy sloupec: y-ove souradnice
plt.scatter(data[:, 0], data[:, 2], c=housings.target, s=2)
plt.title("Classes")

# popisky os
plt.xlabel(housings.feature_names[0])
plt.ylabel(housings.feature_names[2])

# ulozeni diagramu do souboru
plt.savefig("76.png")

# zobrazeni diagramu
plt.show()
