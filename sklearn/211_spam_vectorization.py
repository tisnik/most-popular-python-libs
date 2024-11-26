# Vektorizace textových dat

import pandas as pd 
import re
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

# vektorizace textu
vectorizer = CountVectorizer(
    max_features=2500,
    min_df=7, max_df=0.8, stop_words=stopwords.words("english")
)
vectorized_features = vectorizer.fit_transform(features).toarray()

# slova pro dekódování vah
feature_names = vectorizer.get_feature_names_out()
print("Feature names count:", len(feature_names))
print()

# vlastní výsledek vektorizace
print("Sparse matrix of size", vectorized_features.shape, ":")
print()

# ukázka způsobu zakódování
print("Selected tweet:")
print("Original:     ", features[2])
print("Vectorized:   ", vectorized_features[2])
print()

print("word# weight meaning")
for i, f in enumerate(vectorized_features[2]):
    if f > 0:
        print(f"{i:4}  {f:5}  {feature_names[i]}")