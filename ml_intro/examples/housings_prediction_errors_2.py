import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# nacteni datove sady
housings = fetch_california_housing()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = housings["data"]

# ceny bloku
targets = housings["target"]

# jmena promennych/atributu
names = housings["feature_names"]

print("Ignored attribute\tMSE\tr2 score")

MEASUREMENTS = 200

for column_to_delete in range(len(names)):
    # X je matice, y je vektor
    X = np.delete(data, column_to_delete, axis=1) # smazat jeden vybrany sloupec
    y = targets

    column = names[column_to_delete]

    mses = []
    r2_scores = []

    for i in range(MEASUREMENTS):
        # rozdeleni dat na treninkovou a testovaci mnozinu
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6)

        # konstrukce modelu
        lr = linear_model.LinearRegression()

        # trénink modelu
        lr.fit(X_train, y_train)

        # predikce modelu
        y_pred = lr.predict(X_test)

        # výpis vypočtených koeficientů modelu
        #print("Coefficients: \n", lr.coef_)
        #print("Intercept: \n", lr.intercept_)

        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        mses.append(mse)
        r2_scores.append(r2)

        print(f"{column:16}\t{mse:0.3f}\t{r2:0.3f}")

    plt.plot(range(MEASUREMENTS), mses, range(MEASUREMENTS), r2_scores)

    # titulek grafu
    plt.title(f"Mode prediction without column {column}")
    plt.legend(["MSE", "R2 score"])

    # osy
    plt.xticks()
    plt.yticks()

    # ulozeni diagramu do souboru
    plt.savefig(f"94_{column}.png")

    # zobrazeni diagramu
    plt.show()

