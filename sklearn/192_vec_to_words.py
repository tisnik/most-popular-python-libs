# Realizace zpětného převodu na slova
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


from sklearn.feature_extraction.text import CountVectorizer

# sada textů (korpus)
corpus = [
    "I'd like an apple or an apple pie",
    "An apple a day keeps the doctor away",
    "Never compare an apple to an orange",
    "I prefer scikit-learn to orange",
    "The scikit-learn docs are orange and blue",
    "New apple logo will be orange and blue",
]

# provedení vektorizace korpusu
vectorizer = CountVectorizer(min_df=1)
vectorized = vectorizer.fit_transform(corpus)

# výsledek vektorizace - řídká matice
print(vectorized)
print()

# slova pro dekódování vah
feature_names = vectorizer.get_feature_names_out()
print("Feature names count:", len(feature_names))
print()

# tabulka indexů slov a vlastních slov
print("Index Feature")
for i, feature_name in enumerate(feature_names):
    print(f"{i:2}    {feature_name}")

print()

# převod na běžnou matici
as_array = vectorized.toarray()

# zobrazení výsledku v novém formátu
print(as_array)
print()


def array_to_words(feature_names, as_array):
    """Převod matice s frekvencemi slov zpět na slova."""
    return list(
        feature_names[index]
        for index, included in enumerate(as_array[i])
        if included == 1
    )


# zpětný převod vět
for i in range(len(corpus)):
    print("Original: ", corpus[i])
    print("Vectors:  ", as_array[i])
    print("As words: ", array_to_words(feature_names, as_array))
    print()
