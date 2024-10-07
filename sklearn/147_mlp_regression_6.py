
import matplotlib.pyplot as plt

# model zalozeny na neuronove siti
from sklearn.neural_network import MLPRegressor

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import cross_val_score

# nacteni datove sady
housings = fetch_california_housing()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = housings["data"]

# ceny bloku
targets = housings["target"]

# X je matice, y je vektor
X = data
y = targets

NEURONS = 5
r = range(1, 40)

avg_scores = []

# hledani optimalniho poctu neuronu ve vrstvach
for layers in r:
    # konstrukce modelu
    layer_sizes = (NEURONS, ) * layers
    nn = MLPRegressor(max_iter=5000, hidden_layer_sizes = layer_sizes)

    # vypocet skore
    scores = cross_val_score(nn, X, y, cv=10, scoring="r2", n_jobs=-1)

    # vypsani prumerneho skore do tabulky
    avg_score = scores.mean()
    print(layers, avg_score)

    avg_scores.append(avg_score)

plt.plot(r, avg_scores)
plt.xlabel("Změna počtu vrstev")
plt.ylabel("R2")

# ulozeni grafu do souboru
plt.savefig("147.png")

# vykresleni grafu na obrazovku
plt.show()

