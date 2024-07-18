import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

iris = load_iris()

data = iris.data

fig, axes = plt.subplots(nrows=2, ncols=2)
fig.set_figheight(15)
fig.set_figwidth(15)

for i in range(4):
    ax = axes[i//2][i%2]
    ax.hist(data[:, i], bins=50, histtype="step")
    ax.set(xlabel=iris.feature_names[i])


plt.tight_layout()
plt.savefig("53.png")
plt.show()

