
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score

# model zalozeny na neuronove siti
from sklearn.neural_network import MLPClassifier

# nacteni datove sady
iris = load_iris()

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

avg_scores = []

NEURONS = 5
r = range(1, 40)

# hledani optimalniho poctu neuronu ve vrstvach
for layers in r:
    # konstrukce klasifikatoru
    # (s hyperparametrem)
    layer_sizes = (NEURONS, ) * layers
    classifier = MLPClassifier(max_iter=5000, hidden_layer_sizes = layer_sizes)

    # vypocet skore
    scores = cross_val_score(classifier, X, y, cv=10, scoring="accuracy")

    avg_score = scores.mean()

    # vypsani prumerneho skore do tabulky
    print(layers, avg_score)

    avg_scores.append(avg_score)

plt.plot(r, avg_scores)
plt.xlabel("Změna počtu vrstev")
plt.ylabel("Přesnost modelu")

# ulozeni grafu do souboru
plt.savefig("141.png")

# vykresleni grafu na obrazovku
plt.show()

