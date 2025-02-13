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
# Clanek, kde je tento demonstracni priklad pouzit:
# Datová analýza s využitím nástroje scikit-learn: první kroky
# https://www.root.cz/clanky/datova-analyza-s-vyuzitim-nastroje-scikit-learn-prvni-kroky/
#

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# nacteni datove sady
iris = load_iris()

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

# konstrukce klasifikatoru
# (s hyperparametrem)
classifier = KNeighborsClassifier(n_neighbors=1)

# trening modelu (se vsemi dostupnymi daty)
classifier.fit(X, y)

# parametry jedne rostliny
unknown = [[3, 5, 4, 2]]
print(unknown)

# predikce modelu pro jednu sadu dat
prediction = classifier.predict(unknown)
print(prediction)

# model predikuje hodnoty 0-3, ty si prevedeme na druhy rostlin
print(iris.target_names[prediction])

print()

# parametry vice rostlin
unknown = [[3, 5, 4, 2], [5, 4, 3, 2]]
print(unknown)

# predikce modelu pro vice sad dat
predictions = classifier.predict(unknown)
print(predictions)

# model predikuje hodnoty 0-3, ty si prevedeme na druhy rostlin
print(iris.target_names[predictions])
