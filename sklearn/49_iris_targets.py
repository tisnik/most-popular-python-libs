from sklearn.datasets import load_iris

iris = load_iris()

print(dir(iris))

print("-" * 100)

print("Target names:")
print(iris["target_names"])

print("-" * 100)

print("Targets:")
print(iris["target"])

