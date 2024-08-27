import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn import linear_model
from sklearn.model_selection import cross_val_score

# nacteni datove sady
housings = fetch_california_housing()

# X je matice (feature matrix)
X = housings.data

# y je vektor (response vector)
y = housings.target

feature_names = np.array(housings.feature_names)

print("n", "selectors", "features")

best_score = -1e10
best_selectors = []

for i in range(1, 2**len(feature_names)):
    indexes = []
    n = i
    for j in range(len(feature_names)):
        if n % 2 == 1:
            indexes.append(j)
        n //= 2
    selectors = np.array(indexes, dtype=int)
    # konstrukce modelu
    lr = linear_model.LinearRegression()
    selected_features = X[:, selectors]
    scores = cross_val_score(lr, selected_features, y, cv=10, scoring='r2')
    avg_scores = scores.mean()
    if avg_scores > best_score:
        best_score = avg_scores
        best_selectors = selectors
    print(i, selectors, feature_names[selectors], avg_scores)

print()
print("Best score:", best_score)
print("With features", feature_names[best_selectors])
