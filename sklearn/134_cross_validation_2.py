# import tridy realizujici vyber atributu
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

from sklearn import linear_model

# import funkce pro nacteni datove sady, kterou pouzijeme
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import cross_val_score

# nacteni datove sady
housings = fetch_california_housing()

# jmena jednotlivych atributu
feature_names = housings["feature_names"]

# X je matice (feature matrix)
X = housings.data

# y je vektor (response vector)
y = housings.target

for k_best in range(1, len(feature_names)+1):
    # provest filtering dat
    sel = SelectKBest(f_classif, k=k_best)
    X_new = sel.fit_transform(X, y)

    # konstrukce modelu pro regresi
    lr = linear_model.LinearRegression()
    scores = cross_val_score(lr, X_new, y, cv=10, scoring='r2')

    print(k_best, X_new.shape, sel.get_feature_names_out(input_features=feature_names), scores.mean())
