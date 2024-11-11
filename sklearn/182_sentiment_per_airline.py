# Výpočet hodnocení podle dopravce.

# Založeno na příkladu uvedeného v článku:
# Based on example presented in following article:
# https://stackabuse.com/python-for-nlp-sentiment-analysis-with-scikit-learn/

import pandas as pd

# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# rozdělení hodnocení podle dopravce
airline_sentiment = (
    airline_tweets
    .groupby(["airline", "airline_sentiment"])
    .airline_sentiment.count()
)

# výsledný datový rámec (hierarchický)
print(airline_sentiment)

print()

# pivot tabulka
airline_sentiment = airline_sentiment.unstack()

# výsledný datový rámec
print(airline_sentiment)
