from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

iris = load_iris()

data = iris.data

reduced = PCA(n_components=3).fit_transform(data)

fig, axes = plt.subplots(nrows=2, ncols=2)
fig.set_figheight(15)
fig.set_figwidth(15)

ax = axes[0][0]
scatter = ax.scatter(reduced[:, 0], reduced[:, 1], c=iris.target)

ax = axes[1][0]
scatter = ax.scatter(reduced[:, 0], reduced[:, 2], c=iris.target)

ax = axes[1][1]
scatter = ax.scatter(reduced[:, 1], reduced[:, 2], c=iris.target)

ax = axes[0][1]
fig.delaxes(ax)

plt.tight_layout()
plt.savefig("55.png")
plt.show()

