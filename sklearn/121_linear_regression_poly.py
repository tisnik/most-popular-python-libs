import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

# počet vzorků ve vektorech x i y (delitelne tremi)
VALUES = 120

# x je vektor
x = np.linspace(0, 10, VALUES)

# mensi vektory pro slozeni y
y1 = 0.5*np.random.rand(VALUES//3)
y2 = 1 + 0.5*np.random.rand(VALUES//3)
y3 = 0.5*np.random.rand(VALUES//3)

# y je vektor
y = np.concatenate((y1, y2, y3))

# převod vektoru na 2D matici
X = x.reshape(-1, 1)

# tvar matice X a vektoru y
print("X shape:", X.shape)
print("y shape:", y.shape)

degree = 2

# konstrukce modelu
pr = linear_model.LinearRegression(fit_intercept=False)

poly = PolynomialFeatures(degree=degree)

poly_features = poly.fit_transform(X)

# trénink modelu (X musí být maticí)
pr.fit(poly_features, y)

# predikce modelu
y_pred = pr.predict(poly_features)

# výpis vypočtených koeficientů modelu
print("Coefficients: \n", pr.coef_)
print("Intercept: \n", pr.intercept_)

# vykreslení výsledku
plt.scatter(x, y, color="black", s=2)
plt.plot(x, y_pred, color="blue", linewidth=2)

# titulek grafu
plt.title(f"Degree={degree}")

# osy
plt.xticks(())
plt.yticks(())

# ulozeni diagramu do souboru
plt.savefig("121.png")

# zobrazeni diagramu
plt.show()
