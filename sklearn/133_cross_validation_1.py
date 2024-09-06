# import tridy realizujici vyber atributu
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

from sklearn.neighbors import KNeighborsClassifier

# import funkce pro nacteni datove sady, kterou pouzijeme
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score


# nacteni datove sady
iris = load_iris()

# jmena jednotlivych atributu
feature_names = iris["feature_names"]

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

for k_best in range(1, len(feature_names)+1):
    # provest filtering dat
    sel = SelectKBest(f_classif, k=k_best)
    X_new = sel.fit_transform(X, y)

    print(k_best, X_new.shape, sel.get_feature_names_out(input_features=feature_names))
    # konstrukce klasifikatoru
    knn = KNeighborsClassifier(n_neighbors=5)
    scores = cross_val_score(knn, X_new, y, cv=10, scoring='accuracy')
    print("Average score:", scores.mean())
