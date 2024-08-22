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
from sklearn.model_selection import train_test_split
import numpy as np


# nacteni datove sady
iris = load_iris()


def train_and_predict(training_set_size):
    # konstrukce klasifikatoru
    # (s hyperparametrem)
    classifier = KNeighborsClassifier(n_neighbors=1)

    # X je matice (feature matrix)
    X = iris.data

    # y je vektor (response vector)
    y = iris.target

    # rozdělení na trénovací a testovací data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1.0-training_set_size)
    #print(len(X_train), len(X_test))

    # trening modelu (se vsemi dostupnymi daty)
    classifier.fit(X_train, y_train)

    # očekávané výsledky
    expexted_labels = y_test

    # výsledky modelu (predikované výsledky)
    predicted_labels = classifier.predict(X_test)

    # jak je náš model úspěšný?
    total = 0
    same = 0

    # porovnání predikce s očekáváním
    for (expected, predicted) in zip(expexted_labels, predicted_labels):
        if expected==predicted:
            same+=1
        total+=1

    print(f"{test_size:4.2f}        {total:5}       {same:5}        {100.0*same/total:4.1f}%")


print("Pro trénink    Odhadů    Korektních    Přesnost")

for test_size in np.linspace(0.05, 0.95, 19):
    train_and_predict(test_size)

# finito
