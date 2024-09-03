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
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

# nacteni datove sady
iris = load_iris()


# konstrukce klasifikatoru
# (s hyperparametrem)
knn_1_classifier = KNeighborsClassifier(n_neighbors=1)
knn_2_classifier = KNeighborsClassifier(n_neighbors=5)
lr_classifier_1 = LogisticRegression(max_iter=1)
lr_classifier_2 = LogisticRegression(max_iter=1000)

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target


def score(model):
    scores = cross_val_score(model, X, y, cv=10, scoring='accuracy')
    return scores.mean()


print(f"KNN classifier with K=1:               {score(knn_1_classifier):5.2f}%")
print(f"KNN classifier with K=5:               {score(knn_2_classifier):5.2f}%")
print(f"LogisticRegression with max_iter=1:    {score(lr_classifier_1):5.2f}%")
print(f"LogisticRegression with max_iter=1000: {score(lr_classifier_2):5.2f}%")

# finito
