from sklearn.datasets import fetch_california_housing

# nacteni datove sady
housings = fetch_california_housing()

print(dir(housings))

print("-" * 100)

# podrobny popis datove sady
print(housings["DESCR"])
