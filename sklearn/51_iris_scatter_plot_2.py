import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

# nacteni datove sady
iris = load_iris()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = iris.data

# vykresleni korelacniho diagramu pro dvojici vybranych atributu
_, ax = plt.subplots()
scatter = ax.scatter(data[:, 0], data[:, 1], c=iris.target)

# popisky os
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])

# pridani legendy do diagramu
ax.legend(scatter.legend_elements()[0], iris.target_names, loc="upper right", title="Classes")

# ulozeni diagramu do souboru
plt.savefig("51.png")

# zobrazeni diagramu
plt.show()
