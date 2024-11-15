# Výpočet relevance jednotlivých slov

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# sada textů (korpus)
corpus = [
    "I'd like an apple or an apple pie",
    "An apple a day keeps the doctor away",
    "Never compare an apple to an orange",
    "I prefer scikit-learn to orange",
    "The scikit-learn docs are orange and blue",
    "New apple logo will be orange and blue",
]

# věty pro vyšší četnosti vybraných slov
for i in range(20):
    corpus.append("blue day")

# provedení vektorizace korpusu
vectorizer = CountVectorizer(min_df=1, stop_words="english")
vectorized = vectorizer.fit_transform(corpus)

# slova pro dekódování vah
feature_names = vectorizer.get_feature_names_out()

# převod na běžnou matici
as_array = vectorized.toarray()
print(as_array)

# výpočet IDF - převrácené četnosti slov
transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
transformer.fit(vectorized)

# zobrazení tabulky s převrácenými četnostmi jednotlivých slov
for feature_name, idf in zip(feature_names, transformer.idf_):
    print(f"{feature_name:9} {idf:5.2}")
