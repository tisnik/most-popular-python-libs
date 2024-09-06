# import tridy realizujici vyber atributu
from sklearn.feature_selection import VarianceThreshold

# import funkce pro nacteni datove sady, kterou pouzijeme
from sklearn.datasets import fetch_california_housing

# nacteni datove sady
housings = fetch_california_housing()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = housings["data"]

# tvar puvodni datove sady (pocet zaznamu a atributu) pred vyberem
print("Data shape before selection:")
print(data.shape)

# provest filtering dat
sel = VarianceThreshold(threshold=0.6)
selected = sel.fit_transform(data)

# tvar upravene datove sady (pocet zaznamu a atributu)
print("Data shape after selection:")
print(selected.shape)
