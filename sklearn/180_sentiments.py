# Načtení datové sady a zjištění celkové nálady.

# Založeno na příkladu uvedeného v článku:
# Based on example presented in following article:
# https://stackabuse.com/python-for-nlp-sentiment-analysis-with-scikit-learn/

import pandas as pd 

# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# celková nálada: počty pozitivních, negativních a neutrálních reakcí
print(airline_tweets.airline_sentiment.value_counts())
