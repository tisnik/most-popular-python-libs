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
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

VALUES = 100

x = np.linspace(0, 10, VALUES)
y1 = 0.5*np.random.rand(VALUES//2)
y2 = 1 + 0.5*np.random.rand(VALUES//2)
y = np.concatenate((y1, y2))

for degree in range(1, 12):
    # konstrukce modelu
    pr = linear_model.LinearRegression(fit_intercept=False)

    poly = PolynomialFeatures(degree=degree)

    poly_features = poly.fit_transform(x.reshape(-1, 1))

    # trénink modelu
    pr.fit(poly_features, y)

    # predikce modelu
    y_pred = pr.predict(poly_features)

    # výpis vypočtených koeficientů modelu
    print("Coefficients: \n", pr.coef_)
    print("Intercept: \n", pr.intercept_)

    # chyba predikce
    print("Mean squared error: %.2f" % mean_squared_error(y, y_pred))

    # 1 = nejlepší predikce modelu
    print("Coefficient of determination: %.2f" % r2_score(y, y_pred))

    # vykreslení výsledku
    plt.scatter(x, y, color="black", s=1)
    plt.plot(x, y_pred, color="blue", linewidth=2)

    # titulek grafu
    plt.title(f"Degree={degree}")

    # osy
    plt.xticks(())
    plt.yticks(())

    # ulozeni diagramu do souboru
    plt.savefig(f"83_{degree}.png")

    # zobrazeni diagramu
    plt.show()
