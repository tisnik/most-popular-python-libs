# Načtení datové sady a zjištění počtu tweetů o jednotlivých dopravcích

# Založeno na příkladu uvedeného v článku:
# Based on example presented in following article:
# https://stackabuse.com/python-for-nlp-sentiment-analysis-with-scikit-learn/

import pandas as pd

# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# počet tweetů o jednotlivých dopravcích
print(airline_tweets.airline.value_counts())
