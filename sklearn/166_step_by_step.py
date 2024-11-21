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

import random
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# model zalozeny na neuronove siti
from sklearn.neural_network import MLPRegressor

# velikost vstupu
MAX_N = 40

# X je matice, y je vektor
X = np.zeros( (MAX_N, 2) )   # kombinace vstupu
y = np.zeros( (MAX_N, ))     # vektor vysledku

# zadne skutecne nahodne hodnoty
random.seed(19)

# priprava dat pro trenink i otestovani neuronove site
for i in range(0, MAX_N):
    X[i, 0] = random.randint(-10, 10)
    X[i, 1] = random.randint(-10, 10)
    y[i] = X[i, 1]


# rozdeleni dat na treninkovou a testovaci mnozinu
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


def train_and_test_nn(size: int):
    X_train_ = X_train[:size]
    y_train_ = y_train[:size]

    # konstrukce modelu
    nn = MLPRegressor(max_iter=5000, hidden_layer_sizes=(), random_state=1000)

    # trénink modelu
    nn.fit(X_train_, y_train_)

    # predikce modelu
    y_pred = nn.predict(X_test)

    # chyba predikce
    # 1 = nejlepší predikce modelu
    print("%2d" % size, "%.2f" % mean_squared_error(y_test, y_pred), "%.2f" % r2_score(y_test, y_pred))


# postupne zvetsovani datove sady
for i in range(1, MAX_N+1):
    train_and_test_nn(i)
