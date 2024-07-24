import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

# nacteni datove sady
iris = load_iris()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = iris.data

# vykresleni sady histogramu do mrizky
fig, axes = plt.subplots(nrows=2, ncols=2)
fig.set_figheight(15)
fig.set_figwidth(15)

# vykresleni jednotlivych histogramu do mrizky
for i in range(4):
    ax = axes[i//2][i%2]
    # modifikace zpusobu vypoctu a zobrazeni histogrami
    ax.hist(data[:, i], bins=50, histtype="step")
    ax.set(xlabel=iris.feature_names[i])


# zbavit se prazdneho mista okolo bunek mrizky
plt.tight_layout()

# ulozeni diagramu do souboru
plt.savefig("54.png")

# zobrazeni diagramu
plt.show()

