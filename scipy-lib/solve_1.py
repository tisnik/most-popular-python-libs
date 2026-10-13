# Vyřešení systému lineárních rovnic
# - Triviální příklad - jedna rovnice o jedné neznámé
# - Rovnice 2x = 10
# - Maticově
#      - levá strana rovnice
#      - pravá strana rovnice
#

from scipy import linalg

import numpy as np

# levá strana rovnice (koeficienty)
a = np.array([[2]])

# pravá strana rovnice
b = np.array([10])

# řešení
c = linalg.solve(a, b)

# tisk výsledku operace
print(c)
