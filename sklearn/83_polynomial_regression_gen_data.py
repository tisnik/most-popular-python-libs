import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

VALUES = 50

x = np.linspace(0, 10, VALUES)
y = np.linspace(-1, 1, VALUES) + 0.5*np.random.rand(VALUES)

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
    plt.xticks(())
    plt.yticks(())

    # ulozeni diagramu do souboru
    plt.savefig(f"83_{degree}.png")

    # zobrazeni diagramu
    plt.show()
