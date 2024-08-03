from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# nacteni datove sady
iris = load_iris()


def train_and_predict(training_set_size):
    # konstrukce klasifikatoru
    # (s hyperparametrem)
    classifier = KNeighborsClassifier(n_neighbors=1)

    # počet vzorků pro trénink
    for_training = training_set_size

    # X je matice (feature matrix)
    X = iris.data[:for_training]

    # y je vektor (response vector)
    y = iris.target[:for_training]

    # trening modelu (se vsemi dostupnymi daty)
    classifier.fit(X, y)

    # očekávané výsledky
    expexted_labels = iris.target[for_training:]

    # výsledky modelu (predikované výsledky)
    predicted_labels = classifier.predict(iris.data[for_training:])

    # jak je náš model úspěšný?
    total = 0
    same = 0

    # porovnání predikce s očekáváním
    for (expected, predicted) in zip(expexted_labels, predicted_labels):
        if expected==predicted:
            same+=1
        total+=1

    print(f"{for_training:7}        {total:5}       {same:5}        {100.0*same/total:4.1f}%")


print("Pro trénink    Odhadů    Korektních    Přesnost")

for training_size in np.arange(10, len(iris.data)-10, 10):
    train_and_predict(int(training_size))

# finito
