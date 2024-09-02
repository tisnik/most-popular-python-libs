import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model

# počet vzorků ve vektorech x i y
VALUES = 50

# x je vektor
x = np.linspace(0, 10, VALUES)

# Y je matice vytvořená ze dvou vektorů
y1 = np.linspace(-1, 1, VALUES) + 0.5*np.random.rand(VALUES)
y2 = np.linspace(1, -1, VALUES) + 0.5*np.random.rand(VALUES)

# konstrukce matice se dvěma sloupci
Y= np.column_stack((y1, y2))

# převod vektoru na 2D matici
X = x.reshape(-1, 1)

# tvar matic X a Y
print("X shape:", X.shape)
print("Y shape:", Y.shape)

# konstrukce modelu
lr = linear_model.LinearRegression()

# trénink modelu
lr.fit(X, Y)

# predikce modelu
y_pred = lr.predict(X)

# výpis vypočtených koeficientů modelu
print("Coefficients: \n", lr.coef_)
print("Intercept: \n", lr.intercept_)

for dimension in range(0, 2):
    # vykreslení výsledku
    plt.scatter(x, Y[:, dimension], color="black", s=2)
    plt.plot(x, y_pred[:, dimension], color="blue", linewidth=2)

    # titulek grafu
    plt.title(f"Linear regression in dimension {dimension}")

    # osy
    plt.xticks()
    plt.yticks()

    # ulozeni diagramu do souboru
    plt.savefig(f"115_{dimension}.png")

    # zobrazeni diagramu
    plt.show()

    # druhy diagram
    plt.close()
