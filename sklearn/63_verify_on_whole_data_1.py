from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# nacteni datove sady
iris = load_iris()


# konstrukce klasifikatoru
# (s hyperparametrem)
classifier = KNeighborsClassifier(n_neighbors=1)

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

# trening modelu (se vsemi dostupnymi daty)
classifier.fit(X, y)

# očekávané výsledky
expexted_labels = iris.target

# výsledky modelu (predikované výsledky)
predicted_labels = classifier.predict(iris.data)

# jak je náš model úspěšný?
total = 0
same = 0

# porovnání predikce s očekáváním
for (expected, predicted) in zip(expexted_labels, predicted_labels):
    if expected==predicted:
        same+=1
    total+=1

print("Odhadů    Korektních    Přesnost")
print(f"{total:5}       {same:5}        {100.0*same/total:4.1f}%")

# finito
