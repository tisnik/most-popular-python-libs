# Vizualizace hodnocení podle dopravce.

# Založeno na příkladu uvedeného v článku:
# Based on example presented in following article:
# https://stackabuse.com/python-for-nlp-sentiment-analysis-with-scikit-learn/

import pandas as pd
import matplotlib.pyplot as plt

# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# rozdělení hodnocení podle dopravce
airline_sentiment = (
    airline_tweets
    .groupby(["airline", "airline_sentiment"])
    .airline_sentiment.count()
    .unstack()
)

# zobrazení hodnocení podle dopravce
airline_sentiment.plot(
    kind="bar",
    color=["#ff8080", "yellow", "#80ff80"],
    edgecolor="black",
    figsize=(6, 6),
).legend(loc='best')

plt.tight_layout()

# uložení koláčového diagramu do souboru
plt.savefig("183.png")

# zobrazení koláčového diagramu na obrazovce
plt.show()
