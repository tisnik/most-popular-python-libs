# model zalozeny na neuronove siti
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor

# nacteni datove sady
housings = fetch_california_housing()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = housings["data"]

# ceny bloku
targets = housings["target"]

# X je matice, y je vektor
X = data
y = targets

# rozdeleni dat na treninkovou a testovaci mnozinu
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

# konstrukce modelu
nn = MLPRegressor(max_iter=5000)

# trénink modelu
nn.fit(X_train, y_train)

# predikce modelu
y_pred = nn.predict(X_test)

# chyba predikce
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))

# 1 = nejlepší predikce modelu
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))

print(f"Features: {nn.n_features_in_}")
print(f"Layers:   {nn.n_layers_}")
print(f"Outputs:  {nn.n_outputs_}")
print("Weights:")

for layer, weights in enumerate(nn.coefs_):
    print("\t", layer, weights.shape)

print("Biases:")

for layer, biases in enumerate(nn.intercepts_):
    print("\t", layer, biases.shape)

