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

from sklearn.linear_model import LogisticRegression
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

for_training = len(y) * 8 // 10
print("Vzorků pro trénink:", for_training)

# rozdělení dat
trainX = X[:for_training]
testX = X[for_training:]
trainY = y[:for_training]
testY = y[for_training:]

# provést klasifikaci
# konstrukce klasifikatoru
# (s hyperparametrem)
classifier = LogisticRegression(max_iter=1000)

# vypocet skore
scores = cross_val_score(classifier, X, y, cv=10, scoring="accuracy")
avg_score = scores.mean()
print("Accuracy:", avg_score)

# trening modelu
classifier.fit(trainX, trainY)

predicted_labels = classifier.predict(testX)
images = digits.images[for_training:]

fig = plt.figure(figsize=(6.4, 8.0))

# zobrazit patnáct výsledků
for i in range(25):
    predicted_digit = classifier.predict([testX[i]])[0]
    correct_digit = testY[i]
    print(predicted_digit, correct_digit)
    image = images[i]
    plt.subplot(5, 5, i+1)
    plt.axis("off")
    # zobrazení obrázku
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    # a přidání predikce - o jakou číslici se jedná
    plt.title("Predict: %i" % predicted_digit)

# nakonec vše uložíme a zobrazíme
plt.savefig("158.png")
plt.show()
