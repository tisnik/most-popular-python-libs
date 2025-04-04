from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# nacteni datove sady
iris = load_iris()

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

# konstrukce klasifikatoru
# (s hyperparametrem)
classifier = LogisticRegression(max_iter=1000)
classifier.fit(X, y)

# trening modelu (se vsemi dostupnymi daty)
classifier.fit(X, y)

# parametry jedne rostliny
unknown = [[3, 5, 4, 2]]
print(unknown)

# predikce modelu pro jednu sadu dat
prediction = classifier.predict(unknown)
print(prediction)

# model predikuje hodnoty 0-3, ty si prevedeme na druhy rostlin
print(iris.target_names[prediction])

print()

# parametry vice rostlin
unknown = [[3, 5, 4, 2], [5, 4, 3, 2]]
print(unknown)

# predikce modelu pro vice sad dat
predictions = classifier.predict(unknown)
print(predictions)

# model predikuje hodnoty 0-3, ty si prevedeme na druhy rostlin
print(iris.target_names[predictions])
