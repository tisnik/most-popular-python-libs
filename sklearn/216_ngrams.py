# Vektorizace textových dat s použitím ngramů o délce 1-2 slov, výpis výsledného slovníku

import pandas as pd
import re
from itertools import zip_longest
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

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
    max_features=2500, min_df=7, max_df=0.8, stop_words=stopwords.words("english"), ngram_range=(1,2)
)
vectorized_features = vectorizer.fit_transform(processed_features).toarray()

# slova pro dekódování vah
feature_names = vectorizer.get_feature_names_out()
print("Feature names count:", len(feature_names))
print()

print("Feature names:")
for feature_name in feature_names:
    print(feature_name)
print()

# vlastní výsledek vektorizace
print("Sparse matrix of size", vectorized_features.shape, ":")
print()

# ukázka způsobu zakódování
print("Selected tweet:")
print("Original:     ", features[2])
print("Processed:    ", processed_features[2])
print("Vectorized:   ", vectorized_features[2])
print()

print("word# weight meaning")
for i, f in enumerate(vectorized_features[2]):
    if f > 0:
        print(f"{i:4}  {f:5}  {feature_names[i]}")
