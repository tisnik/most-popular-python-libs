import numpy as np

# import funkce pro nacteni datove sady, kterou pouzijeme
from sklearn.datasets import fetch_california_housing

# nacteni datove sady
housings = fetch_california_housing()

# precteni dat z datove sady
data = housings["data"]

# nadpis tabulky
print("Feature              Min         Max           Avg         Std         Var")

# zakladni statisticke informace o jednotlivych atributech
for i in range(len(housings["feature_names"])):
    column = data[:, i]
    feature = housings.feature_names[i]
    print(f"{feature:12}   {column.min():10.3f}   {column.max():10.3f}   {np.mean(column):10.3f}  {np.std(column):10.3f}  {np.var(column):11.3f}")
