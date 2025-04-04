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
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

# model zalozeny na neuronove siti
from sklearn.neural_network import MLPClassifier


# nacteni datove sady
iris = load_iris()

# konstrukce klasifikatoru
# (s hyperparametrem)
classifier = MLPClassifier(max_iter=5000, hidden_layer_sizes = (10, 10, 10))

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

# rozdělení na trénovací a testovací data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# trening modelu
classifier.fit(X_train, y_train)


# výsledky modelu (predikované výsledky)
y_pred = classifier.predict(X_test)

# vypoctena presnost modelu
print(accuracy_score(y_test, y_pred))

print(f"Features: {classifier.n_features_in_}")
print(f"Layers:   {classifier.n_layers_}")
print(f"Outputs:  {classifier.n_outputs_}")
print("Weights:")

for layer, weights in enumerate(classifier.coefs_):
    print("\t", layer, weights.shape)

print("Biases:")

for layer, biases in enumerate(classifier.intercepts_):
    print("\t", layer, biases.shape)

