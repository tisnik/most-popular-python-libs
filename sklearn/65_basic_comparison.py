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
from sklearn.linear_model import LogisticRegression

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

# trening modelu (se vsemi dostupnymi daty)
knn_1_classifier.fit(X, y)
knn_2_classifier.fit(X, y)
lr_classifier_1.fit(X, y)
lr_classifier_2.fit(X, y)


def score(model):
    # očekávané výsledky
    expexted_labels = iris.target

    # výsledky modelu (predikované výsledky)
    predicted_labels = model.predict(iris.data)

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
