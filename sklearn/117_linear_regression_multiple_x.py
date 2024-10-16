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

from sklearn import linear_model

# počet vzorků v mřížce
VALUES = 20

# X je matice vytvořená z mřížky
# dvojice vektorů pro konstrukci mřížky
x1 = np.linspace(1, 100, VALUES)
x2 = np.linspace(1, 100, VALUES)

# konstrukce mřížky
grid = np.meshgrid(x1, x2)

# změna tvaru na matici se dvěma sloupci
X = np.vstack([grid[0].flatten(), grid[1].flatten()]).T

# y je vektor
y = (grid[0] + grid[1]).flatten()

# tvar matice X a vektoru y
print("X shape:", X.shape)
print("y shape:", y.shape)

# konstrukce modelu
lr = linear_model.LinearRegression()

# trénink modelu
lr.fit(X, y)

# predikce modelu
y_pred = lr.predict(X).reshape((VALUES, VALUES))
print(y_pred)

# výpis vypočtených koeficientů modelu
print("Coefficients: \n", lr.coef_)
print("Intercept: \n", lr.intercept_)

# vykreslení výsledku do 3D grafu
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(projection="3d")

# body ze vstupní datové sady
ax.scatter(X[:, 0], X[:, 1], y, color="black", s=2)

# výsledkem modelu je rovina
ax.plot_surface(grid[0], grid[1], y_pred, alpha = 0.5)

# ulozeni diagramu do souboru
plt.savefig("117.png")

# zobrazeni diagramu
plt.show()
