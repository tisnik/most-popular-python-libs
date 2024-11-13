# Nalezení textu, který se nejvíce blíží hledanému vzorku

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

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
vectorizer = TfidfVectorizer(min_df=1, stop_words="english")
vectorized = vectorizer.fit_transform(corpus)

# výsledek vektorizace - řídká matice
print(vectorized)
print()

# matice s převrácenými četnostmi
pairwise_similarity = vectorized * vectorized.T

print(pairwise_similarity)
print()

print(pairwise_similarity.toarray())
print()

arr = pairwise_similarity.toarray()

# odstranění jedniček na hlavní diagonále
np.fill_diagonal(arr, np.nan)
print(arr)
print()

# hledaná věta
input_doc = "New apple logo will be orange and blue"
input_idx = corpus.index(input_doc)
print(input_idx, input_doc)

result_idx = np.nanargmax(arr[input_idx])
print(result_idx, corpus[result_idx])
