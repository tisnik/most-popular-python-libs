from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# model zalozeny na neuronove siti
from sklearn.neural_network import MLPClassifier

# nacteni datove sady
iris = load_iris()

# konstrukce klasifikatoru
# (s hyperparametrem)
classifier = MLPClassifier(max_iter=5000)

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

# rozdělení na trénovací a testovací data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# trening modelu
classifier.fit(X_train, y_train)

# očekávané výsledky
expexted_labels = y_test

# výsledky modelu (predikované výsledky)
predicted_labels = classifier.predict(X_test)

# jak je náš model úspěšný?
total = 0
same = 0

# porovnání predikce s očekáváním
for (expected, predicted) in zip(expexted_labels, predicted_labels):
    if expected==predicted:
        same+=1
    total+=1

print(f"total:    {total}")
print(f"same:     {same}")
print(f"accuracy: {100.0*same/total:4.1f}%")

print(f"Features: {classifier.n_features_in_}")
print(f"Layers:   {classifier.n_layers_}")
print(f"Outputs:  {classifier.n_outputs_}")
print("Weights:")

for layer, weights in enumerate(classifier.coefs_):
    print("\t", layer, weights.shape)

print("Biases:")

for layer, biases in enumerate(classifier.intercepts_):
    print("\t", layer, biases.shape)

