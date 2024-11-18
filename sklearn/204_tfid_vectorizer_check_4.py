import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# sada textů (korpus)
corpus = [
    "foo bar baz",
    "apple orange",
    "Go foo",
]

# provedení vektorizace korpusu
vectorizer = TfidfVectorizer(min_df=1)
vectorized = vectorizer.fit_transform(corpus)

# slova pro dekódování vah
feature_names = vectorizer.get_feature_names_out()
for index, feature in enumerate(feature_names):
    print(index, feature)
print()

# výsledek vektorizace - řídká matice: převod na běžnou matici
as_array = vectorized.toarray()

# zobrazení výsledku v novém formátu
np.set_printoptions(precision=2)
print(as_array)
