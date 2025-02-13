# Načtení datové sady a zjištění základních informací o v ní uložených datech.

# Založeno na příkladu uvedeného v článku:
# Based on example presented in following article:
# https://stackabuse.com/python-for-nlp-sentiment-analysis-with-scikit-learn/

import pandas as pd 

# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# zobrazení prvních deseti řádků tabulky
print(airline_tweets.head())

print()

# zobrazení posledních deseti řádků tabulky
print(airline_tweets.tail())
