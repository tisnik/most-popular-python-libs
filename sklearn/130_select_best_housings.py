# import tridy realizujici vyber atributu
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

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

# provest filtering dat
sel = SelectKBest(f_classif, k=4)
selected = sel.fit_transform(data, housings["target"])

# tvar upravene datove sady (pocet zaznamu a atributu)
print("Data shape after selection:")
print(selected.shape)
print(sel.get_feature_names_out(input_features=housings["feature_names"]))
