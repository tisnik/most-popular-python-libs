# Vektorizace sady textů (korpusu)

import numpy as np
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

# převod na běžnou matici
as_array = vectorized.toarray()

# zobrazení výsledku v novém formátu
print(as_array)
print()

# získat vektor z 2D pole
flattened = as_array.flatten()

# unikátní prvky a jejich frekvence
unique, counts = np.unique(flattened, return_counts=True)

print("Word count statistic:")
print(np.asarray((unique, counts)).T)
