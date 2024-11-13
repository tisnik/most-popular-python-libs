# Tabulka pro zpětný převod indexů na slova

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
