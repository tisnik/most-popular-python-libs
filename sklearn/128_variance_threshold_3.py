import numpy as np

# import tridy realizujici vyber atributu
from sklearn.feature_selection import VarianceThreshold

# import funkce pro nacteni datove sady, kterou pouzijeme
from sklearn.datasets import load_iris

# nacteni datove sady
iris = load_iris()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = iris["data"]

# jmena jednotlivych atributu
feature_names = iris["feature_names"]

# tvar puvodni datove sady (pocet zaznamu a atributu) pred vyberem
print("Data shape before selection:")
print(data.shape)

# jmena vsech puvodnich atributu
print("Features before selection:")
print(feature_names)

print()

for threshold in np.linspace(0.0, 1.0, 11):
    sel = VarianceThreshold(threshold=threshold)

    selected = sel.fit_transform(data)

    print(threshold, selected.shape, sel.get_feature_names_out(input_features=feature_names))
