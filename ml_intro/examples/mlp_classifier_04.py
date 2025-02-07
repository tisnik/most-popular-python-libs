
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

r = range(1, 20)

# hledani optimalniho poctu neuronu ve vrstvach
for neurons in r:
    # konstrukce klasifikatoru
    # (s hyperparametrem)
    classifier = MLPClassifier(max_iter=5000, hidden_layer_sizes = (neurons, neurons, neurons))

    # vypocet skore
    scores = cross_val_score(classifier, X, y, cv=10, scoring="accuracy")

    avg_score = scores.mean()

    # vypsani prumerneho skore do tabulky
    print(neurons, avg_score)

    avg_scores.append(avg_score)

plt.plot(r, avg_scores)
plt.xlabel("Změna počtu neuronů ve třech vrstvách")
plt.ylabel("Přesnost modelu")

# ulozeni grafu do souboru
plt.savefig("139.png")

# vykresleni grafu na obrazovku
plt.show()

