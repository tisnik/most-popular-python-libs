# Vektorizace textových dat, výpis výsledného slovníku
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
    max_features=2500, min_df=7, max_df=0.8, stop_words=stopwords.words("english")
)
vectorized_features = vectorizer.fit_transform(processed_features).toarray()

# slova pro dekódování vah
feature_names = vectorizer.get_feature_names_out()
print("Feature names count:", len(feature_names))
print("Feature names:")

columns = 4
for c1, c2, c3, c4 in zip_longest(
    feature_names[::columns],
    feature_names[1::columns],
    feature_names[2::columns],
    feature_names[3::columns],
):
    print(f"{str(c1): <20}{str(c2): <20}{str(c3): <20}{c4}")
