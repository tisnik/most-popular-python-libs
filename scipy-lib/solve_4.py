# Pokus o vyřešení systému lineárních rovnic
#  - Dvě rovnice o dvou neznámých
#       - x + y = 2
#       - 2x + 2y = 4
#  - Rovnice 2 je lineární kombinací rovnice 1
#  - Maticově
#      - levé strany rovnic
#      - pravé strany rovnic
# 

import numpy as np
from scipy import linalg

# levá strana rovnice (koeficienty)
# matice koeficientů původních rovnic
# [1,1] znamená 1*x + 1*y
a = np.array([[1, 1], [2, 2]])

# matice pravých stran rovnic
b = np.array([2, 4])

# řešení
c = linalg.solve(a, b)

# tisk výsledku operace
print(c)
