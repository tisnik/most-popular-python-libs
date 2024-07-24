import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

# nacteni datove sady
iris = load_iris()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = iris.data

# vykresleni korelacniho diagramu pro dvojici vybranych atributu
plt.scatter(data[:, 0], data[:, 1], c=iris.target)
plt.title("Classes")

# popisky os
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

# ulozeni diagramu do souboru
plt.savefig("50.png")

# zobrazeni diagramu
plt.show()
