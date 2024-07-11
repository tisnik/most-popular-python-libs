import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

iris = load_iris()

data = iris.data

reduced = PCA(n_components=3).fit_transform(data)

fig = plt.figure(1)
ax = fig.add_subplot(111, projection="3d", elev=-150, azim=110)

reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(
    reduced[:, 0],
    reduced[:, 1],
    reduced[:, 2],
    c=iris.target,
    s=40,
)

plt.tight_layout()
plt.savefig("56.png")
plt.show()

