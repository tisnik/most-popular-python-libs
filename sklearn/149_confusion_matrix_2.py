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
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import ConfusionMatrixDisplay

# nacteni datove sady
iris = load_iris()

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

# rozdělení dat
trainX, testX, trainY, testY = train_test_split(X, y, test_size = 0.5)

# konstrukce klasifikatoru
# (s hyperparametrem)
classifier = KNeighborsClassifier(n_neighbors=5)

# trening modelu (se vsemi dostupnymi daty)
classifier.fit(trainX, trainY)

y_pred = classifier.predict(testX)

print(classification_report(testY, y_pred))

class_names = iris.target_names

# absolutni hodnoty
disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    testX,
    testY,
    display_labels=class_names,
    cmap=plt.cm.Blues,
    normalize=None,
)

# zobrazeni matice
print(disp.confusion_matrix)

# ulozeni vysledku
plt.savefig("149_1.png")

# vizualizace matice
plt.show()

# relativni hodnoty
disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    testX,
    testY,
    display_labels=class_names,
    cmap=plt.cm.Blues,
    normalize="true",
)

# zobrazeni matice
print(disp.confusion_matrix)

# ulozeni vysledku
plt.savefig("149_2.png")

# vizualizace matice
plt.show()
