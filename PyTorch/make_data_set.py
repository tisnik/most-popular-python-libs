# Knihovna PyTorch
#
# - výpočet trénovacích a testovacích dat pro neuronové sítě

# budeme provádět vykreslování de facto standardní knihovnou Matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

# testovací data
n_samples = 2000

samples, labels = make_circles(
    n_samples=n_samples, factor=0.5, noise=0.05
)

# rozdělení na trénovací a testovací množinu
X_train, X_test, y_train, y_test = train_test_split(samples, labels, test_size=1/3, random_state=26)

# vizualizace
fig, (train_ax, test_ax) = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(10, 5))
train_ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=plt.cm.Set1)
train_ax.set_title("Trénovací data")
train_ax.set_xlabel("Feature #0")
train_ax.set_ylabel("Feature #1")

test_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=plt.cm.Set1)
test_ax.set_xlabel("Feature #0")
test_ax.set_title("Testovací data")

# uložení grafu do souboru
plt.savefig("circles4.png")

# vykreslení na obrazovku
plt.show()
