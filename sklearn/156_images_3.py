# Rozpoznání obrazu s využitím knihovny scikit-learn

import matplotlib.pyplot as plt
import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import cross_val_score

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

# rozdělení dat
trainX, testX, trainY, testY = train_test_split(X, y, test_size = 0.2)

print()
print("TrainX:", trainX.shape)
print("TrainY:", trainY.shape)
print("TestX:", testX.shape)
print("TestY:", testY.shape)

# provést klasifikaci
# konstrukce klasifikatoru
# (s hyperparametrem)
classifier = KNeighborsClassifier(n_neighbors=5)

# vypocet skore
scores = cross_val_score(classifier, X, y, cv=10, scoring="accuracy")

avg_score = scores.mean()

# vypsani prumerneho skore
print()
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

# ulozeni vysledku
plt.savefig("156_1.png")

# vizualizace matice
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
plt.savefig("156_2.png")

# vizualizace matice
plt.show()
