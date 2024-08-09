from sklearn.datasets import fetch_california_housing

# nacteni datove sady
housings = fetch_california_housing()

# jmena atributu
print("Feature names:")
print(housings["feature_names"])

print("-" * 100)

# vazba mezi numerickou hodnotou a lidskym vyjadrenim hodnoty
# atributu
print("Target names:")
print(housings["target_names"])

print("-" * 100)

# druhy rostlin z datove sady v numericke podobe
print("Targets:")
print(housings["target"])

