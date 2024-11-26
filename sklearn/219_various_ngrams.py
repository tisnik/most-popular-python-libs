# Trénink a predikce modelu nad vektorizovanými daty, založeno na třídě TfidfVectorizer, použití ngramů

import pandas as pd
import re
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
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


def model_with_ngrams(min_ngrams, max_ngrams, detailed_report):

    # vektorizace textu
    vectorizer = TfidfVectorizer(
        max_features=5000, min_df=7, max_df=0.8,
        stop_words=stopwords.words("english"), ngram_range=(min_ngrams, max_ngrams)
    )
    vectorized_features = vectorizer.fit_transform(processed_features).toarray()
    columns = vectorized_features.shape[1]

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
    if detailed_report:
        print(classification_report(testY, predictions))
        print()

        # matice záměn - absolutní hodnoty
        disp = ConfusionMatrixDisplay.from_estimator(
            classifier,
            testX,
            testY,
            normalize=None,
        )

        # zobrazení matice v textové podobě
        print(disp.confusion_matrix)
        print()

        # matice záměn - relativní hodnoty
        disp = ConfusionMatrixDisplay.from_estimator(
            classifier,
            testX,
            testY,
            normalize="true",
        )

        # zobrazení matice v textové podobě
        print(disp.confusion_matrix)

    score = accuracy_score(testY, predictions)
    print(f"{min_ngrams}  {max_ngrams}  {columns:4}  {score:05.3}")


for min_ngrams in range(1, 7):
    for max_ngrams in range(min_ngrams, 8):
        model_with_ngrams(min_ngrams, max_ngrams, False)
