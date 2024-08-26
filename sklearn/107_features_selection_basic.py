import numpy as np
from sklearn.datasets import load_iris

# nacteni datove sady
iris = load_iris()

feature_names = np.array(iris.feature_names)

print("n", "selectors", "features")

for i in range(1, 2**len(feature_names)):
    indexes = []
    n = i
    for j in range(len(feature_names)):
        if n % 2 == 1:
            indexes.append(j)
        n //= 2
    selectors = np.array(indexes, dtype=int)
    print(i, selectors, feature_names[selectors])

