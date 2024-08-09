import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

# nacteni datove sady
housings = fetch_california_housing()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = housings["data"]

# vykresleni mrizky korelacnich diagramu
fig, axes = plt.subplots(nrows=8, ncols=8)

# rozmery vysledneho obrazku
fig.set_figheight(15)
fig.set_figwidth(15)

# vyplneni mrizky
for row in range(8):
    for column in range(8):
        ax = axes[row][column]
        if row == column:
            # na diagonale jsou prazdna mista
            fig.delaxes(ax)
            continue
        # pridat korelacni diagram do mrizky
        # sloupec row: x-ove souradnice
        # sloupec column: y-ove souradnice
        scatter = ax.scatter(data[:, row], data[:, column], c=housings.target, s=1)
        # popisky os
        ax.set(xlabel=housings.feature_names[row], ylabel=housings.feature_names[column])


# zbavit se prazdneho mista okolo bunek mrizky
plt.tight_layout()

# ulozeni diagramu do souboru
plt.savefig("77.png")

# zobrazeni diagramu
plt.show()
