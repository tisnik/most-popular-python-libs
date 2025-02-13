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
# Tento demonstracni priklad je pouzity v serialu o datove analyze
# s vyuzitim programovaciho jazyka Python:
# https://www.root.cz/serialy/datova-analyza-s-vyuzitim-jazyka-python/
#
# Clanek, kde je tento demonstracni priklad pouzit:
# Balíček scikit-learn: modely provádějící klasifikaci
# https://www.root.cz/clanky/balicek-scikit-learn-modely-provadejici-klasifikaci/
#

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

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

# rozdělení na trénovací a testovací data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

# trening modelu (se vsemi dostupnymi daty)
knn_1_classifier.fit(X_train, y_train)
knn_2_classifier.fit(X_train, y_train)
lr_classifier_1.fit(X_train, y_train)
lr_classifier_2.fit(X_train, y_train)


def score(model):
    # očekávané výsledky
    expexted_labels = y_test

    # výsledky modelu (predikované výsledky)
    predicted_labels = model.predict(X_test)

    # jak je náš model úspěšný?
    total = 0
    same = 0

    # porovnání predikce s očekáváním
    for (expected, predicted) in zip(expexted_labels, predicted_labels):
        if expected==predicted:
            same+=1
        total+=1
    return 100.0*same/total


print(f"KNN classifier with K=1:               {score(knn_1_classifier):5.2f}%")
print(f"KNN classifier with K=5:               {score(knn_2_classifier):5.2f}%")
print(f"LogisticRegression with max_iter=1:    {score(lr_classifier_1):5.2f}%")
print(f"LogisticRegression with max_iter=1000: {score(lr_classifier_2):5.2f}%")

# finito
