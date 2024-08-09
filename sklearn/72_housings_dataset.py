from sklearn.datasets import fetch_california_housing

# nacteni datove sady
housings = fetch_california_housing()

# jakeho typu je vlastne datova sada?
print(type(housings))

print("-" * 100)

# dostupne atributy a metody
print(dir(housings))
