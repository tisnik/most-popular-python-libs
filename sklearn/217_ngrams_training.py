# Trénink a predikce modelu nad vektorizovanými daty, založeno na třídě CountVectorizer, použití ngramů
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


import pandas as pd
import re
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import classification_report, accuracy_score
from sklearn.neighbors import KNeighborsClassifier

# načtení tabulky do datového rámce, specifikace kódování souboru
spam = pd.read_csv("spam.csv", encoding="latin1")

# hodnocení (spam/ham)
labels = spam.v1.values

# vlastní text SMS
features = spam.v2.values

# hodnoty použité později pro trénink modelu
print("Labels:")
print(labels)
print("Number of labels:", len(labels))
print()

print("Features:")
print(features)
print("Number of features:", len(features))
print()


def process_feature(feature):
    """Preprocesing textových dat."""
    # odstranění speciálních znaků a dalšího smetí
    processed_feature = re.sub(r"\W", " ", feature)

    # odstranění samostatných znaků (oddělených bílými znaky)
    processed_feature = re.sub(r"\s+[a-zA-Z]\s+", " ", processed_feature)

    # odstranění samostatných znaků na začátku vět
    processed_feature = re.sub(r"\^[a-zA-Z]\s+", " ", processed_feature)

    # náhrada více mezer (nebo jiných bílých znaků) za jedinou mezeru
    processed_feature = re.sub(r"\s+", " ", processed_feature, flags=re.I)

    # odstranění slov s číslicemi
    processed_feature = re.sub("\w*\d\w*", "", processed_feature)

    # odstranění prefixů ^b
    processed_feature = re.sub(r"^b\s+", "", processed_feature)

    # odstranění znaků, které nejsou ASCII
    processed_feature = processed_feature.encode("ascii", errors="ignore").decode()

    # konverze výsledku na malá písmena
    return processed_feature.strip().lower()


# preprocesing všech hodnocení
processed_features = [process_feature(feature) for feature in features]

# vektorizace textu
vectorizer = CountVectorizer(
    max_features=2500, min_df=7, max_df=0.8, stop_words=stopwords.words("english"), ngram_range=(1, 2)
)
vectorized_features = vectorizer.fit_transform(processed_features).toarray()

# klasické rozdělení datové sady na trénovací a testovací část
trainX, testX, trainY, testY = train_test_split(
    vectorized_features, labels, test_size=0.2, random_state=0
)

# konstrukce vybraného modelu s předáním hyperparametrů
classifier = KNeighborsClassifier(n_neighbors=1)

# trénink modelu
classifier.fit(trainX, trainY)

# predikce modelu pro testovací vstupy (ne pro trénovací data)
predictions = classifier.predict(testX)

# vyhodnocení kvality modelu
print(classification_report(testY, predictions))
print("Accuracy score:", accuracy_score(testY, predictions))
print()

# matice záměn - absolutní hodnoty
disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    testX,
    testY,
    cmap=plt.cm.Blues,
    normalize=None,
)

# zobrazení matice v textové podobě
print(disp.confusion_matrix)
print()

# uložení výsledků ve formě rastrového obrázku
plt.savefig("217_1.png")

# vizualizace matice
plt.show()

# matice záměn - relativní hodnoty
disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    testX,
    testY,
    cmap=plt.cm.Blues,
    normalize="true",
)

# zobrazení matice v textové podobě
print(disp.confusion_matrix)

# uložení výsledků ve formě rastrového obrázku
plt.savefig("217_2.png")

# vizualizace matice
plt.show()
