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

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score


# nacteni datove sady
iris = load_iris()

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

best_score = 0
best_index = -1

# hledani optimalniho poctu regionu pro KNN
for k in range(1, 50):
    # konstrukce klasifikatoru
    knn = KNeighborsClassifier(n_neighbors=k)

    # vypocet skore
    scores = cross_val_score(knn, X, y, cv=10, scoring="accuracy")

    avg_score = scores.mean()

    # dosahli jsme lepsiho ohodnoceni?
    if avg_score > best_score:
        best_index = k
        best_score = avg_score

    # vypsani prumerneho skore do tabulky
    print(k, avg_score)

print()
print(f"Best score {best_score} for K={best_index}")
