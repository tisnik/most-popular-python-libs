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
from sklearn.metrics import mean_squared_error, r2_score

VALUES = 100

x = np.linspace(0, 10, VALUES)
y1 = 0.5*np.random.rand(VALUES//2)
y2 = 1 + 0.5*np.random.rand(VALUES//2)

# nelinearita - skok
y = np.concatenate((y1, y2))

# konstrukce modelu
lr = linear_model.LinearRegression()

# trénink modelu
lr.fit(x.reshape(-1, 1), y)

# predikce modelu
y_pred = lr.predict(x.reshape(-1, 1))

# výpis vypočtených koeficientů modelu
print("Coefficients: \n", lr.coef_)
print("Intercept: \n", lr.intercept_)

# chyba predikce
print("Mean squared error: %.2f" % mean_squared_error(y, y_pred))

# 1 = nejlepší predikce modelu
print("Coefficient of determination: %.2f" % r2_score(y, y_pred))

# vykreslení výsledku
plt.scatter(x, y, color="black", s=2)
plt.plot(x, y_pred, color="blue", linewidth=2)

# titulek grafu
plt.title("Linear regression")

# osy
plt.xticks()
plt.yticks()

# ulozeni diagramu do souboru
plt.savefig("88.png")

# zobrazeni diagramu
plt.show()
