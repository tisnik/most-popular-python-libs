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

for k_best in range(0, len(feature_names)+1):
    # provest filtering dat
    sel = SelectKBest(f_classif, k=k_best)
    selected = sel.fit_transform(data, housings["target"])

    print(k_best, selected.shape, sel.get_feature_names_out(input_features=feature_names))
