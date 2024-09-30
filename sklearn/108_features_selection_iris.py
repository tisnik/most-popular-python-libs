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

import numpy as np
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

# nacteni datove sady
iris = load_iris()

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

feature_names = np.array(iris.feature_names)

print("n", "selectors", "features")

for i in range(1, 2**len(feature_names)):
    indexes = []
    n = i
    for j in range(len(feature_names)):
        if n % 2 == 1:
            indexes.append(j)
        n //= 2
    selectors = np.array(indexes, dtype=int)
    knn_classifier = KNeighborsClassifier(n_neighbors=5)
    selected_features = X[:, selectors]
    scores = cross_val_score(knn_classifier, selected_features, y, cv=10, scoring="accuracy")
    print(i, selectors, feature_names[selectors], scores.mean())

