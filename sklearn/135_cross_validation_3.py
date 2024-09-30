# import tridy realizujici vyber atributu
from sklearn.feature_selection import VarianceThreshold

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

sel = VarianceThreshold(threshold=0.6)
X_new = sel.fit_transform(X, y)

# konstrukce modelu pro regresi
lr = linear_model.LinearRegression()
scores = cross_val_score(lr, X_new, y, cv=10, scoring="r2")

print(X_new.shape, sel.get_feature_names_out(input_features=feature_names), scores.mean())
