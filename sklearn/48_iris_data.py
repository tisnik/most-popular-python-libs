from sklearn.datasets import load_iris

iris = load_iris()

print(dir(iris))

print("-" * 100)

print("Feature names:")
print(iris["feature_names"])

print("-" * 100)

print("Feature data:")
print(iris["data"])
