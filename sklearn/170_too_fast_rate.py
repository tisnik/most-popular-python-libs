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
import numpy as np

import random
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# model zalozeny na neuronove siti
from sklearn.neural_network import MLPRegressor

# velikost vstupu
MAX_N = 50

# X je matice, y je vektor
X = np.zeros( (MAX_N, 2) )   # kombinace vstupu
y = np.zeros( (MAX_N, ))     # vektor vysledku

random.seed(19)

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
    nn = MLPRegressor(max_iter=5000, hidden_layer_sizes=(), random_state=1000, learning_rate_init=0.2)

    # trénink modelu
    nn.fit(X_train_, y_train_)

    # predikce modelu
    y_pred = nn.predict(X_test)

    # chyba predikce
    # 1 = nejlepší predikce modelu
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print("%2d" % size, "%.2f" % mse, "%.2f" % r2)

    # vahy na vstupu neuronu ve vystupni vrstve
    w = nn.coefs_[0]

    # bias na vstupu neuronu ve vystupni vrstve
    b = nn.intercepts_[0]

    # vratit obe vahy i bias
    return mse, r2, w[0][0], w[1][0], b[0]


# trening site az do poctu prvku MAX_N
r = range(1, MAX_N+1)

weights1 = []
weights2 = []
biases = []
mses = []
r2s = []

# postupne provest treing site, vyplneni poli s vahami a biasy
for i in r:
    mse, r2, weight1, weight2, bias = train_and_test_nn(i)
    mses.append(mse)
    r2s.append(r2)
    weights1.append(weight1)
    weights2.append(weight2)
    biases.append(bias)

print(weights1)
print(weights2)
print(biases)

plt.plot(r, mses, r, r2s)
plt.legend(["MSE", "R2 score"])
plt.savefig("mse_r2.png")
plt.show()

plt.plot(r, weights1, r, weights2)
plt.legend(["weight1", "weight2"])
plt.savefig("weights.png")
plt.show()

plt.plot(r, biases)
plt.legend(["bias"])
plt.savefig("biases.png")
plt.show()
