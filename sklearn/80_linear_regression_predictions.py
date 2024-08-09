import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

VALUES = 100

x = np.linspace(0, 10, VALUES)
y = np.linspace(-1, 1, VALUES) + 0.5*np.random.rand(VALUES)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.6)

print("Array sizes:")
print(f"x_train: {len(x_train)}")
print(f"y_train: {len(y_train)}")
print(f"x_test:  {len(x_test)}")
print(f"y_test:  {len(y_test)}")

# konstrukce modelu
lr = linear_model.LinearRegression()

# trénink modelu
lr.fit(x_train.reshape(-1, 1), y_train)

# predikce modelu
y_pred = lr.predict(x_test.reshape(-1, 1))

1# výpis vypočtených koeficientů modelu
print("Coefficients: \n", lr.coef_)

# vykreslení výsledku
plt.scatter(x_test, y_test, color="black", s=2)
plt.plot(x_test, y_pred, color="blue", linewidth=2)

# titulek grafu
plt.title("Linear regression")

# osy
plt.xticks(())
plt.yticks(())

# ulozeni diagramu do souboru
plt.savefig("80.png")

# zobrazeni diagramu
plt.show()
