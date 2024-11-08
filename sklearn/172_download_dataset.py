# Stažení datové sady, kterou budeme používat v dalších demonstračních
# příkladech.

import requests

url = "https://raw.githubusercontent.com/satyajeetkrjha/kaggle-Twitter-US-Airline-Sentiment-/refs/heads/master/Tweets.csv"

response = requests.get(url)

with open("Tweets_airlines.csv", "wb") as fout:
    fout.write(response.content)
