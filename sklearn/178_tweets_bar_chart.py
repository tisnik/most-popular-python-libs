# Vykreslení sloupcového diagramu s počty tweetů o jednotlivých dopravcích

# Založeno na příkladu uvedeného v článku:
# Based on example presented in following article:
# https://stackabuse.com/python-for-nlp-sentiment-analysis-with-scikit-learn/

import pandas as pd
import matplotlib.pyplot as plt

# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# specifikace plochy grafu
fig = plt.figure(1, figsize=(6, 6), dpi=150)

# vykreslení sloupcového diagramu s počty tweetů o jednotlivých dopravcích
airline_tweets.airline.value_counts().plot(
    kind="bar",
)

# zajištění místa pro popisky os
fig.tight_layout()

# uložení sloupcového diagramu do souboru
plt.savefig("178.png")

# zobrazení diagramu na obrazovce
plt.show()
