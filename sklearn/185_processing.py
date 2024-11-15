# Preprocesing textových dat

# Založeno na příkladu uvedeného v článku:
# Based on example presented in following article:
# https://stackabuse.com/python-for-nlp-sentiment-analysis-with-scikit-learn/

import pandas as pd
import re

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

# porovnání výsledků preprocesingu
for i in range(10):
    print(features[i], " | ", processed_features[i])
