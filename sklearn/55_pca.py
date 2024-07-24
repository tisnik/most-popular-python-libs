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

# vykresleni vysledku do matice s diagramy
fig, axes = plt.subplots(nrows=2, ncols=2)
fig.set_figheight(15)
fig.set_figwidth(15)

# graf v matici
ax = axes[0][0]
scatter = ax.scatter(reduced[:, 0], reduced[:, 1], c=iris.target)

# graf v matici
ax = axes[1][0]
scatter = ax.scatter(reduced[:, 0], reduced[:, 2], c=iris.target)

# graf v matici
ax = axes[1][1]
scatter = ax.scatter(reduced[:, 1], reduced[:, 2], c=iris.target)

# prazdne misto v matici
ax = axes[0][1]
fig.delaxes(ax)

# zbavit se prazdneho mista okolo bunek mrizky
plt.tight_layout()

# ulozeni diagramu do souboru
plt.savefig("55.png")

# zobrazeni diagramu
plt.show()

