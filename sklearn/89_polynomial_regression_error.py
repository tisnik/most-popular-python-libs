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

degrees = []
mses = []
r2_scores = []

for degree in range(1, 50):
    # konstrukce modelu
    pr = linear_model.LinearRegression(fit_intercept=False)

    poly = PolynomialFeatures(degree=degree)

    poly_features = poly.fit_transform(x.reshape(-1, 1))

    # trénink modelu
    pr.fit(poly_features, y)

    # predikce modelu
    y_pred = pr.predict(poly_features)

    degrees.append(degree)
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    mses.append(mse)
    r2_scores.append(r2)
    print(degree, mse, r2)


plt.plot(degrees, mses, degrees, r2_scores)

# titulek grafu
plt.title("Mode prediction")
plt.legend(["MSE", "R2 score"])

# osy
plt.xticks()
plt.yticks()

# ulozeni diagramu do souboru
plt.savefig("89.png")

# zobrazeni diagramu
plt.show()

