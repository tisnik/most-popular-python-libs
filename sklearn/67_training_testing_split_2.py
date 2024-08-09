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

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.utils import shuffle
import numpy as np


# nacteni datove sady
iris = load_iris()


def train_and_predict(training_set_size):
    # konstrukce klasifikatoru
    # (s hyperparametrem)
    classifier = KNeighborsClassifier(n_neighbors=1)

    # počet vzorků pro trénink
    for_training = training_set_size

    # kopie poli (abychom nemenili puvodni data)
    data = np.copy(iris.data)
    targets = np.copy(iris.target)

    # zamichani obou poli se zarucenim, ze bude zachovan vztah data:target
    data, targets = shuffle(data, targets)

    # X je matice (feature matrix)
    X = data[:for_training]

    # y je vektor (response vector)
    y = targets[:for_training]

    # trening modelu (se vsemi dostupnymi daty)
    classifier.fit(X, y)

    # očekávané výsledky
    expexted_labels = targets[for_training:]

    # výsledky modelu (predikované výsledky)
    predicted_labels = classifier.predict(data[for_training:])

    # jak je náš model úspěšný?
    total = 0
    same = 0

    # porovnání predikce s očekáváním
    for (expected, predicted) in zip(expexted_labels, predicted_labels):
        if expected==predicted:
            same+=1
        total+=1

    print(f"{for_training:7}        {total:5}       {same:5}        {100.0*same/total:4.1f}%")


print("Pro trénink    Odhadů    Korektních    Přesnost")

for training_size in np.arange(10, len(iris.data)-10, 10):
    train_and_predict(int(training_size))

# finito
