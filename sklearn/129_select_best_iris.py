# import tridy realizujici vyber atributu
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

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

# provest filtering dat
sel = SelectKBest(f_classif, k=2)
selected = sel.fit_transform(data, iris["target"])

# tvar upravene datove sady (pocet zaznamu a atributu)
print("Data shape after selection:")
print(selected.shape)
print(sel.get_feature_names_out(input_features=iris["feature_names"]))
