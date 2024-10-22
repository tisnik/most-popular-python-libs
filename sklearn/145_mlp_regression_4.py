#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#
#
# Tento demonstracni priklad je pouzity v serialu o datove analyze
# s vyuzitim programovaciho jazyka Python:
# https://www.root.cz/serialy/datova-analyza-s-vyuzitim-jazyka-python/
#


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

r = range(1, 12)
avg_scores = []

# hledani optimalniho poctu neuronu ve vrstvach
for i in r:
    # konstrukce modelu
    neurons = 2**i
    nn = MLPRegressor(max_iter=5000, hidden_layer_sizes = (neurons, neurons, neurons))

    scores = cross_val_score(nn, X, y, cv=10, scoring="r2")

    # vypsani prumerneho skore do tabulky
    avg_score = scores.mean()
    print(neurons, avg_score)

    avg_scores.append(avg_score)

plt.plot(r, avg_scores)
plt.xlabel("Změna počtu neuronů ve třech vrstvách")
plt.ylabel("R2")

# ulozeni grafu do souboru
plt.savefig("145.png")

# vykresleni grafu na obrazovku
#plt.show()

