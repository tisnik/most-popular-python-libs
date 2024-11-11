# Načtení datové sady a získání vlastních tweetů a hodnocení

# Založeno na příkladu uvedeného v článku:
# Based on example presented in following article:
# https://stackabuse.com/python-for-nlp-sentiment-analysis-with-scikit-learn/

import pandas as pd 

# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# hodnocení (pozitivní, negativní, neutrální)
labels = airline_tweets["airline_sentiment"].values

# vlastní text hodnocení
features = airline_tweets["text"].values

# hodnoty použité později pro trénink modelu
print("Labels:")
print(labels)
print("Number of labels:", len(labels))
print()

print("Features:")
print(features)
print("Number of features:", len(features))
