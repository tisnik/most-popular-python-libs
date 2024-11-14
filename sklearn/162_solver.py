#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#
#
# Tento demonstracni priklad je pouzity v serialu o datove analyze
# s vyuzitim programovaciho jazyka Python:
# https://www.root.cz/serialy/datova-analyza-s-vyuzitim-jazyka-python/
#

# Rozpoznání obrazu s využitím knihovny scikit-learn

import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import ConfusionMatrixDisplay

# Databáze ručně zapsaných číslic
from sklearn.datasets import load_digits

# načtení obrázků, s nimiž budeme dále pracovat
digits = load_digits()

# zjištění základních informací o obrázcích
print("Description:", digits.DESCR)

print("Data:", digits.data.shape)
print("Obrázky:", digits.images.shape)

# X je matice (feature matrix)
X = digits.data

# y je vektor (response vector)
y = digits.target

for_training = len(y) * 8 // 10
print("Vzorků pro trénink:", for_training)
print("\n\n")

# rozdělení dat
trainX = X[:for_training]
testX = X[for_training:]
trainY = y[:for_training]
testY = y[for_training:]


def train_and_test_model(solver: str, show_results: bool = False):
    print(f"Neural network with solver '{solver}'")

    # provést klasifikaci
    # konstrukce klasifikatoru
    # (s hyperparametrem)
    classifier = MLPClassifier(max_iter=5000, solver=solver)

    # vypocet skore
    scores = cross_val_score(classifier, X, y, cv=10, scoring="accuracy")

    avg_score = scores.mean()

    # vypsani prumerneho skore
    print("Accuracy:", avg_score)
    print()

    # trening modelu
    classifier.fit(trainX, trainY)

    class_names = digits.target_names

    # absolutni hodnoty
    disp = ConfusionMatrixDisplay.from_estimator(
        classifier,
        testX,
        testY,
        display_labels=class_names,
        cmap=plt.cm.Blues,
        normalize=None,
    )

    # zobrazeni matice
    print(disp.confusion_matrix)
    print()

    # ulozeni vysledku
    plt.savefig(f"{solver}_confusion_matrix_abs.png")

    # vizualizace matice
    if show_results:
        plt.show()

    # relativni hodnoty
    disp = ConfusionMatrixDisplay.from_estimator(
        classifier,
        testX,
        testY,
        display_labels=class_names,
        cmap=plt.cm.Blues,
        normalize="true",
    )

    # zobrazeni matice
    print(disp.confusion_matrix)

    # ulozeni vysledku
    plt.savefig(f"{solver}_confusion_matrix_rel.png")

    # vizualizace matice
    if show_results:
        plt.show()

    predicted_labels = classifier.predict(testX)
    images = digits.images[for_training:]

    fig = plt.figure(figsize=(6.4, 10.0))

    # zobrazit patnáct výsledků
    wrong = 0
    i = 0
    while wrong < 30:
        predicted_digit = classifier.predict([testX[i]])[0]
        correct_digit = testY[i]
        if predicted_digit != correct_digit:
            image = images[i]
            wrong += 1
            plt.subplot(6, 5, wrong)
            plt.axis("off")
            # zobrazení obrázku
            plt.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
            # a přidání predikce - o jakou číslici se jedná
            plt.title(f"{predicted_digit} <> {correct_digit}")
        i += 1
        # nenasli jsme vice cislic
        if i >= len(testX):
            break

    # nakonec vše uložíme a zobrazíme
    plt.savefig(f"{solver}_wrong_digits.png")
    if show_results:
        plt.show()
    print()
    print("-" * 70)
    return avg_score


solvers = ("lbfgs", "sgd", "adam")

scores = []

for solver in solvers:
    score = train_and_test_model(solver)
    scores.append(score)

fig, ax = plt.subplots()

ax.bar(solvers, scores)

ax.set_ylabel("Model accuracy")
ax.set_title("Solver")

plt.savefig("accuracy.png")
plt.show()
