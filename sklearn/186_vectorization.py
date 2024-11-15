# Vektorizace textových dat

# Založeno na příkladu uvedeného v článku:
# Based on example presented in following article:
# https://stackabuse.com/python-for-nlp-sentiment-analysis-with-scikit-learn/

import pandas as pd
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer



# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# hodnocení (pozitivní, negativní, neutrální)
labels = airline_tweets["airline_sentiment"].values

# vlastní text hodnocení
features = airline_tweets["text"].values


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

    # odstranění prefixů ^b
    processed_feature = re.sub(r"^b\s+", "", processed_feature)

    # konverze výsledku na malá písmena
    return processed_feature.lower()


# preprocesing všech hodnocení
processed_features = [process_feature(feature) for feature in features]

# hodnoty použité později pro trénink modelu
print("Labels:")
print(labels)
print("Number of labels:", len(labels))
print()

print("Features:")
print(processed_features)
print("Number of features:", len(processed_features))
print()

# vektorizace textu
vectorizer = CountVectorizer(
    max_features=2500,
    min_df=7, max_df=0.8, stop_words=stopwords.words("english")
)
vectorized_features = vectorizer.fit_transform(processed_features).toarray()

# slova pro dekódování vah
feature_names = vectorizer.get_feature_names_out()
print("Feature names count:", len(feature_names))
print("Feature names:")
for feature_name in feature_names:
    print(feature_name)

print()

# vlastní výsledek vektorizace
print("Sparse matrix of size", vectorized_features.shape, ":")
print(vectorized_features)
print()

# ukázka způsobu zakódování
print("Selected tweet:")
print("Original:     ", features[2])
print("Preprocessed: ", processed_features[2])
print("Vectorized:   ", vectorized_features[2])
print()

print("word# weight meaning")
for i, f in enumerate(vectorized_features[2]):
    if f > 0:
        print(f"{i:4}  {f:5}  {feature_names[i]}")
