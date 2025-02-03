import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

# nacteni datove sady
housings = fetch_california_housing()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = housings["data"]

# vykresleni sady histogramu do mrizky
fig, axes = plt.subplots(nrows=4, ncols=2)
fig.set_figheight(15)
fig.set_figwidth(15)

# vykresleni jednotlivych histogramu do mrizky
for i in range(8):
    column = data[:, i]
    feature = housings.feature_names[i]
    ax = axes[i//2][i%2]
    # modifikace zpusobu vypoctu a zobrazeni histogrami
    ax.hist(column, bins=100, histtype="step")
    ax.set(xlabel=feature)


# zbavit se prazdneho mista okolo bunek mrizky
plt.tight_layout()

# ulozeni diagramu do souboru
plt.savefig("95.png")

# zobrazeni diagramu
plt.show()
