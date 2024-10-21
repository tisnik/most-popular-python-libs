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
import matplotlib.pyplot as plt

# model zalozeny na neuronove siti
from sklearn.neural_network import MLPRegressor

# velikost tabulky soucinu
MAX_N = 10

# X je matice, y je vektor
X = np.zeros( (MAX_N*MAX_N, 2) )   # kombinace cinitelu
y = np.zeros( (MAX_N*MAX_N, ))     # vektor soucinu
i = 0
for a in range(1, MAX_N+1):
    for b in range(1, MAX_N+1):
        X[i, 0] = a                # cinitel
        X[i, 1] = b                # cinitel
        y[i] = a * b               # soucin
        i+=1

# konstrukce modelu
nn = MLPRegressor(max_iter=5000, hidden_layer_sizes=(100, 100))

# trénink modelu nad vsemi daty
nn.fit(X, y)

# zobrazit parametry neuronove site
print(f"Features: {nn.n_features_in_}")
print(f"Layers:   {nn.n_layers_}")
print(f"Outputs:  {nn.n_outputs_}")
print("Weights:")

# vahy neuronu
for layer, weights in enumerate(nn.coefs_):
    print("\t", layer, weights.shape)

# posuny (dalsi vstup do neuronu)
print("Biases:")
for layer, biases in enumerate(nn.intercepts_):
    print("\t", layer, biases.shape)

MAX_TO_COMPUTE = 20

X2 = np.zeros( (MAX_TO_COMPUTE*MAX_TO_COMPUTE, 2) )   # kombinace cinitelu
y2 = np.zeros( (MAX_TO_COMPUTE*MAX_TO_COMPUTE, ))     # vektor soucinu
i = 0
for a in range(1, MAX_TO_COMPUTE+1):
    for b in range(1, MAX_TO_COMPUTE+1):
        X2[i, 0] = a                # cinitel
        X2[i, 1] = b                # cinitel
        y2[i] = a * b               # soucin
        i+=1

# odhady (odpovedi) neuronove site po uprave do matice 10x10
Z = nn.predict(X2).round().reshape((MAX_TO_COMPUTE, MAX_TO_COMPUTE))

print("Prediction:")
print(Z)

# korektni tabulka male nasobilky
W = y2.reshape((MAX_TO_COMPUTE, MAX_TO_COMPUTE))

print("Relative errors:")
errors = (100*(Z-W)/W).astype("int")
print(errors)

# vizualizace chyb
plt.matshow(Z-W)

# ulozeni vysledku
plt.savefig("153.png")

# zobrazeni
plt.show()
