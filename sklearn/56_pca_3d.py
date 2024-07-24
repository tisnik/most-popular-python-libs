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
