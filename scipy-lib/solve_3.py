# Vyřešení systému lineárních rovnic
#  - Tři rovnice o třech neznámých
#
#     2x₁ + 3x₂ + 7x₃ = 47
#     3x₁ + 8x₂ +  x₃ = 50
#           3x₂ + 3x₃ = 27
# 

import numpy as np
from scipy import linalg

# levá strana rovnice (koeficienty)
# matice koeficientů původních rovnic
a = np.array([[2, 3, 7], [3, 8, 1], [0, 3, 3]])

# matice pravých stran rovnic
b = np.array([47, 50, 27])

# řešení
c = linalg.solve(a, b)

# tisk výsledku operace
print(c)
