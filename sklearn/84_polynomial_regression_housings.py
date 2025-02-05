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

import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.datasets import fetch_california_housing

# nacteni datove sady
housings = fetch_california_housing()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = housings["data"]

# serazeni dat (pro pekne grafy)
data = data[data[:,6].argsort()]

FIRST_DIM = 6
SECOND_DIM = 7

x = data[:, FIRST_DIM]
y = data[:, SECOND_DIM]

for degree in range(1, 11):
    # konstrukce modelu
    pr = linear_model.LinearRegression()

    poly = PolynomialFeatures(degree=degree)

    poly_features = poly.fit_transform(x.reshape(-1, 1))

    # trénink modelu
    pr.fit(poly_features, y)

    # predikce modelu
    y_pred = pr.predict(poly_features)

    # výpis vypočtených koeficientů modelu
    print("Coefficients: \n", pr.coef_)
    print("Intercept: \n", pr.intercept_)

    # vykreslení výsledku
    plt.scatter(x, y, color="black", s=1)
    plt.plot(x, y_pred, color="blue", linewidth=2)

    # titulek grafu
    plt.title(f"Degree={degree}")

    # osy
    plt.xlabel(housings.feature_names[FIRST_DIM])
    plt.ylabel(housings.feature_names[SECOND_DIM])
    plt.xticks(())
    plt.yticks(())

    # ulozeni diagramu do souboru
    plt.savefig(f"84_{degree}.png")

    # zobrazeni diagramu
    plt.show()
