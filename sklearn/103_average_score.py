from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score


# nacteni datove sady
iris = load_iris()

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

# konstrukce klasifikatoru
knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
print("Scores:")
for i, score in enumerate(scores):
    print(i, score)

# prumer skore
print()
print("Average score:", scores.mean())

# search for an optimal value of K for KNN
k_range = list(range(1, 31))
k_scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
    k_scores.append(scores.mean())
print(k_scores)
