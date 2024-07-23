from sklearn.datasets import load_iris

# nacteni datove sady
iris = load_iris()

print(dir(iris))

print("-" * 100)

# jmena atributu
print("Feature names:")
print(iris["feature_names"])

print("-" * 100)

# vazba mezi numerickou hodnotou a lidskym vyjadrenim hodnoty
# atributu
print("Target names:")
print(iris["target_names"])

print("-" * 100)

# druhy rostlin z datove sady v numericke podobe
print("Targets:")
print(iris["target"])

