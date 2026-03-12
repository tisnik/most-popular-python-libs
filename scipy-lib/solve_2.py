# Vyřešení systému lineárních rovnic
#  - Dvě rovnice o dvou neznámých
#       - x + y = 2
#       - x - y = 0
#  - Maticově
#      - levé strany rovnic
#      - pravé strany rovnic
# 

import numpy as np
from scipy import linalg

# levá strana rovnice (koeficienty)
# matice koeficientů původních rovnic
# [1,1] znamená 1*x + 1*y
a = np.array([[1, 1], [1, -1]])

# matice pravých stran rovnic
b = np.array([2, 0])

# řešení
c = linalg.solve(a, b)

# tisk výsledku operace
print(c)
