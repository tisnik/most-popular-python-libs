# Načtení datové sady a vizualizace celkové nálady.

# Založeno na příkladu uvedeného v článku:
# Based on example presented in following article:
# https://stackabuse.com/python-for-nlp-sentiment-analysis-with-scikit-learn/

import pandas as pd
import matplotlib.pyplot as plt

# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# plocha grafu
fig = plt.figure(1, figsize=(6, 6), dpi=150)

# vykreslení koláčového diagramu s hodnoceními
airline_tweets.airline_sentiment.value_counts().plot(
    kind="pie",
    autopct="%1.0f%%",
    colors=["#ff8080", "yellow", "#80ff80"],
    wedgeprops={"edgecolor": "black", "linewidth": 2, "antialiased": True},
)

# uložení koláčového diagramu do souboru
plt.savefig("181.png")

# zobrazení koláčového diagramu na obrazovce
plt.show()
