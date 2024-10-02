import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# model zalozeny na neuronove siti
from sklearn.neural_network import MLPRegressor

# velikost tabulky soucinu
MAX_N = 10

# X je matice, y je vektor
X = np.zeros( (MAX_N*MAX_N, 2) )   # kombinace cinitelu
y = np.zeros( (MAX_N*MAX_N, ))     # vektor soucinu
i = 0
for a in range(1, MAX_N+1):
    for b in range(1, MAX_N+1):
        X[i, 0] = a                # cinitel
        X[i, 1] = b                # cinitel
        y[i] = a * b               # soucin
        i+=1

# rozdeleni dat na treninkovou a testovaci mnozinu
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

# konstrukce modelu
nn = MLPRegressor(max_iter=5000, hidden_layer_sizes=(100, 100))

# trénink modelu
nn.fit(X_train, y_train)

# predikce modelu
y_pred = nn.predict(X_test)

# chyba predikce
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))

# 1 = nejlepší predikce modelu
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))

# zobrazit parametry neuronove site
print(f"Features: {nn.n_features_in_}")
print(f"Layers:   {nn.n_layers_}")
print(f"Outputs:  {nn.n_outputs_}")
print("Weights:")

# vahy neuronu
for layer, weights in enumerate(nn.coefs_):
    print("\t", layer, weights.shape)

# posuny (dalsi vstup do neuronu)
print("Biases:")
for layer, biases in enumerate(nn.intercepts_):
    print("\t", layer, biases.shape)

# nezname vstupy
inputs = [[1, 1], [2,  3], [5, 5], [4, 10], [10, 4], [9, 9], [10, 10]]
predicted = nn.predict(inputs)

# odhady neuronove site bez dalsich uprav
print("w/o rounding:")
for i, p in zip(inputs, predicted):
    print(f"{i[0]:2} * {i[1]:2} = {p:6.2f}")

# odhady neuronove site po zaokrouhleni
print("rounded:")
for i, p in zip(inputs, predicted):
    print(f"{i[0]:2} * {i[1]:2} = {int(p):2}")
