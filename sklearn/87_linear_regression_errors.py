import numpy as np
from sklearn import linear_model
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def errors_and_score_for_linear_regression(x_train, x_test, y_train, y_test):
    # konstrukce modelu
    lr = linear_model.LinearRegression()

    # trénink modelu
    lr.fit(x_train.reshape(-1, 1), y_train)

    # predikce modelu
    y_pred = lr.predict(x_test.reshape(-1, 1))

    # výpis vypočtených koeficientů modelu
    print("    Coefficients:      ", lr.coef_)
    print("    Intercept:         ", lr.intercept_)

    # chyba predikce
    print("    Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))

    # 1 = nejlepší predikce modelu
    print("    Coefficient of determination: %.2f" % r2_score(y_test, y_pred))
    print()



# ------------------------------------------------------------------------
# zcela nenáhodná data

VALUES = 100

x = np.linspace(0, 10, VALUES)
y = np.linspace(-1, 1, VALUES)

# rozdělení na trénovací a testovací data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.6)

print("Non-random data that are on one line:")
errors_and_score_for_linear_regression(x_train, x_test, y_train, y_test)



# ------------------------------------------------------------------------
# data obsahující náhodné odchylky

VALUES = 100

x = np.linspace(0, 10, VALUES)
y = np.linspace(-1, 1, VALUES) + 0.5*np.random.rand(VALUES)

# rozdělení na trénovací a testovací data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.6)

print("Data with added randomness that are on one line:")
errors_and_score_for_linear_regression(x_train, x_test, y_train, y_test)



# ------------------------------------------------------------------------
# zcela náhodná data

VALUES = 100

x = np.linspace(0, 10, VALUES)
y = -1 + 2*np.random.rand(VALUES)

# rozdělení na trénovací a testovací data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.6)

print("Totally random data:")
errors_and_score_for_linear_regression(x_train, x_test, y_train, y_test)



# ------------------------------------------------------------------------
# California housings

# nacteni datove sady
housings = fetch_california_housing()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = housings["data"]

FIRST_DIM = 6
SECOND_DIM = 7

# rozdělení na trénovací a testovací data
x_train, x_test, y_train, y_test = train_test_split(data[:, FIRST_DIM], data[:, SECOND_DIM], test_size=0.6)

print("California housings data: longitude/lattitude:")
errors_and_score_for_linear_regression(x_train, x_test, y_train, y_test)
