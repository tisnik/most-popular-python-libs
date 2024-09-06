# import tridy realizujici vyber atributu
from sklearn.feature_selection import VarianceThreshold

# import funkce pro nacteni datove sady, kterou pouzijeme
from sklearn.datasets import fetch_california_housing

# nacteni datove sady
housings = fetch_california_housing()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = housings["data"]

# jmena jednotlivych atributu
feature_names = housings["feature_names"]

# tvar puvodni datove sady (pocet zaznamu a atributu) pred vyberem
print("Data shape before selection:")
print(data.shape)

# jmena vsech puvodnich atributu
print("Features before selection:")
print(feature_names)

print()

sel = VarianceThreshold(threshold=0.6)
selected = sel.fit_transform(data)

# tvar upravene datove sady (pocet zaznamu a atributu)
print("Data shape after selection:")
print(selected.shape)

# jmena vybranych atributu
print("Features after selection:")
print(sel.get_feature_names_out(input_features=housings["feature_names"]))
