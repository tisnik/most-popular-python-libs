from sklearn.svm import LinearSVC

# import funkce pro nacteni datove sady, kterou pouzijeme
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel

# nacteni datove sady
iris = load_iris()

# ziskani atributu a ocekavanych vysledku
X = iris["data"]
y = iris["target"]

# jmena jednotlivych atributu
feature_names = iris["feature_names"]

# "odhadovac" vysledku
lsvc = LinearSVC(C=0.01, penalty="l1", dual=False).fit(X, y)

# vyber modelu
model = SelectFromModel(lsvc, prefit=True)

# tisk modelu
print(model)

# transformace dat
X_new = model.transform(X)

# natrenovani modelu
model.fit(X, y)

# vysledek + ziskani jmen atributu, ktere se pouzily
print(X_new.shape)
print(model.get_feature_names_out(input_features=feature_names))

