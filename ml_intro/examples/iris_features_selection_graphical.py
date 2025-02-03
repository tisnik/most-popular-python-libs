import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

# nacteni datove sady
iris = load_iris()

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

feature_names = np.array(iris.feature_names)

print("n", "selectors", "features")

attributes = []
final_scores = []

for i in range(1, 2**len(feature_names)):
    indexes = []
    n = i
    for j in range(len(feature_names)):
        if n % 2 == 1:
            indexes.append(j)
        n //= 2
    selectors = np.array(indexes, dtype=int)
    knn_classifier = KNeighborsClassifier(n_neighbors=5)
    selected_features = X[:, selectors]
    scores = cross_val_score(knn_classifier, selected_features, y, cv=10, scoring="accuracy")
    attributes.append("\n".join(feature_names[selectors]))
    avg_score = scores.mean()
    final_scores.append(avg_score)
    print(i, selectors, feature_names[selectors], avg_score)

fig = plt.figure()
fig.set_figwidth(14)
fig.set_figheight(6)
fig.subplots_adjust(bottom=0.3)

plt.bar(attributes, final_scores)
plt.xticks(rotation=90)
plt.xlabel("Atributy")
plt.ylabel("Přesnost modelu")

# ulozeni grafu do souboru
plt.savefig("111.png")

# vykresleni grafu na obrazovku
plt.show()

