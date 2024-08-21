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

import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# nacteni datove sady
housings = fetch_california_housing()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = housings["data"]

# ceny bloku
targets = housings["target"]

# jmena promennych/atributu
names = housings["feature_names"]

print("MSE\tr2 score")

# X je matice, y je vektor
X = data
y = targets

mses = []
r2_scores = []

MEASUREMENTS = 200

for i in range(MEASUREMENTS):
    # rozdeleni dat na treninkovou a testovaci mnozinu
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6)

    # konstrukce modelu
    lr = linear_model.LinearRegression()

    # trénink modelu
    lr.fit(X_train, y_train)

    # predikce modelu
    y_pred = lr.predict(X_test)

    # výpis vypočtených koeficientů modelu
    #print("Coefficients: \n", lr.coef_)
    #print("Intercept: \n", lr.intercept_)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    mses.append(mse)
    r2_scores.append(r2)

    print(f"{mse:0.3f}\t{r2:0.3f}")

plt.plot(range(MEASUREMENTS), mses, range(MEASUREMENTS), r2_scores)

# titulek grafu
plt.title(f"Mode prediction")
plt.legend(["MSE", "R2 score"])

# osy
plt.xticks()
plt.yticks()

# ulozeni diagramu do souboru
plt.savefig(f"93.png")

# zobrazeni diagramu
plt.show()

