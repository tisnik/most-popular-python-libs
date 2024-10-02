import numpy as np
import matplotlib.pyplot as plt

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

# konstrukce modelu
nn = MLPRegressor(max_iter=5000, hidden_layer_sizes=(100, 100))

# trénink modelu nad vsemi daty
nn.fit(X, y)

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

# odhady (odpovedi) neuronove site po uprave do matice 10x10
Z = nn.predict(X).round().reshape((MAX_N, MAX_N))

print("Prediction:")
print(Z)

# korektni tabulka male nasobilky
W = y.reshape((MAX_N, MAX_N))

print("Relative errors:")
errors = (100*(Z-W)/W).astype("int")
print(errors)

# vizualizace chyb
plt.matshow(Z-W)

# ulozeni vysledku
plt.savefig("152.png")

# zobrazeni
plt.show()
