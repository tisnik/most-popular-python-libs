#!/usr/bin/env python

# import funkce, která vrátí obrázky pro práci
from sklearn.datasets import load_digits

import numpy as np

# načtení obrázků, s nimiž budeme dále pracovat
digits_data = load_digits()

# celkový počet vzorků
samples = len(digits_data.images)
print("Vzorků celkem:", samples)
print()

# vytvoření seznamu, které použijeme 
images = list(zip(digits_data.target, digits_data.images))


def train_and_predict(training_set_size):
    # počet vzorků pro trénink
    for_training = training_set_size

    # obrázky (ve formě vektoru) a jejich označení
    training_images = digits_data.data[:for_training]
    training_labels = digits_data.target[:for_training]

    # provést klasifikaci
    from sklearn import svm
    classify = svm.SVC(gamma=0.001)
    classify.fit(training_images, training_labels)

    # očekávané výsledky vs. výsledky modelu
    expexted_labels = digits_data.target[for_training:]
    predicted_labels = classify.predict(digits_data.data[for_training:])

    # jak je náš model úspěšný?
    total = 0
    same = 0

    for (expected, predicted) in zip(expexted_labels, predicted_labels):
        if expected==predicted:
            same+=1
        total+=1

    print(f"{for_training:7}        {total:5}       {same:5}        {100.0*same/total:4.1f}%")


print("Pro trénink    Odhadů    Korektních    Přesnost")

for training_size in np.linspace(10, samples-100, 15):
    train_and_predict(int(training_size))

# finito
