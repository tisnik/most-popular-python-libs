import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model

VALUES = 50

x = np.linspace(0, 10, VALUES)
y = np.linspace(-1, 1, VALUES) + 0.5*np.random.rand(VALUES)

# konstrukce modelu
lr = linear_model.LinearRegression()

# trénink modelu
lr.fit(x.reshape(-1, 1), y)

# predikce modelu
y_pred = lr.predict(x.reshape(-1, 1))

1# výpis vypočtených koeficientů modelu
print("Coefficients: \n", lr.coef_)

# vykreslení výsledku
plt.scatter(x, y, color="black", s=2)
plt.plot(x, y_pred, color="blue", linewidth=2)

# titulek grafu
plt.title("Linear regression")

# osy
plt.xticks(())
plt.yticks(())

# ulozeni diagramu do souboru
plt.savefig("79.png")

# zobrazeni diagramu
plt.show()
