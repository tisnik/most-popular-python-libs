import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

iris = load_iris()

data = iris.data

fig, axes = plt.subplots(nrows=4, ncols=4)
fig.set_figheight(15)
fig.set_figwidth(15)

for row in range(0, 4):
    for column in range(0, 4):
        ax = axes[row][column]
        if row == column:
            fig.delaxes(ax)
            continue
        scatter = ax.scatter(data[:, row], data[:, column], c=iris.target)
        ax.set(xlabel=iris.feature_names[row], ylabel=iris.feature_names[column])


plt.tight_layout()
plt.savefig("52.png")
plt.show()

