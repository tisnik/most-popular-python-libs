# Trénink a predikce modelu nad vektorizovanými daty

# Založeno na příkladu uvedeného v článku:
# Based on example presented in following article:
# https://stackabuse.com/python-for-nlp-sentiment-analysis-with-scikit-learn/

import numpy as np
import pandas as pd
import re
import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# model zalozeny na neuronove siti
from sklearn.neural_network import MLPClassifier



# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# hodnocení (pozitivní, negativní, neutrální)
labels = airline_tweets["airline_sentiment"].values

# vlastní text hodnocení
features = airline_tweets["text"].values


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

    # odstranění prefixů ^b
    processed_feature = re.sub(r"^b\s+", "", processed_feature)

    # konverze výsledku na malá písmena
    return processed_feature.lower()


# preprocesing všech hodnocení
processed_features = [process_feature(feature) for feature in features]

# hodnoty použité později pro trénink modelu
print("Labels:")
print(labels)
print("Number of labels:", len(labels))
print()

print("Features:")
print(processed_features)
print("Number of features:", len(processed_features))
print()

# vektorizace textu
vectorizer = TfidfVectorizer(
    max_features=2500, min_df=7, max_df=0.8, stop_words=stopwords.words("english")
)
vectorized_features = vectorizer.fit_transform(processed_features).toarray()

# klasické rozdělení datové sady na trénovací a testovací část
trainX, testX, trainY, testY = train_test_split(
    vectorized_features, labels, test_size=0.2, random_state=0
)

# konstrukce vybraného modelu s předáním hyperparametrů
classifier =  MLPClassifier(max_iter=5000)

# trénink modelu
classifier.fit(trainX, trainY)

# predikce modelu pro testovací vstupy (ne pro trénovací data)
predictions = classifier.predict(testX)

# vyhodnocení kvality modelu
print(classification_report(testY, predictions))
print(accuracy_score(testY, predictions))

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

# uložení výsledků ve formě rastrového obrázku
plt.savefig("189_1.png")

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
plt.savefig("189_2.png")

# vizualizace matice
plt.show()
