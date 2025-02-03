import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# nacteni datove sady
housings = fetch_california_housing()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = housings["data"]

FIRST_DIM = 2
SECOND_DIM = 3

# rozdělení na trénovací a testovací data
x_train, x_test, y_train, y_test = train_test_split(data[:, FIRST_DIM], data[:, SECOND_DIM], test_size=0.6)

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

# výpis vypočtených koeficientů modelu
print("Coefficients: \n", lr.coef_)
print("Intercept: \n", lr.intercept_)

# chyba predikce
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))

# 1 = nejlepší predikce modelu
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))

# vykreslení výsledku
plt.scatter(x_test, y_test, color="black", s=1)
plt.plot(x_test, y_pred, color="blue", linewidth=3)

# osy
plt.xlabel(housings.feature_names[FIRST_DIM])
plt.ylabel(housings.feature_names[SECOND_DIM])
plt.xticks(())
plt.yticks(())

# ulozeni diagramu do souboru
plt.savefig("82.png")

# zobrazeni diagramu
plt.show()
