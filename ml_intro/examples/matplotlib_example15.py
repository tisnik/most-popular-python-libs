# - sloupcový graf se dvěma skupinami sloupců

import matplotlib.pyplot as plt
import numpy as np

# první pole hodnot
vals1 = [10, 15, 20, 12, 14, 8]

# druhé pole hodnot
vals2 = [19, 18, 6, 11, 6, 14]

# počet prvků
N = len(vals1)

# indexy prvků
indexes = np.arange(N)

# šířka sloupců
width = 0.30

# sloupcový graf se dvěma skupinami sloupců
plt.bar(indexes, vals1, width, color="gray", edgecolor="black", label="CPU#1")
# posunuté sloupce
plt.bar(indexes + width, vals2, width, color="red", edgecolor="black", label="CPU#2")

# povolení zobrazení mřížky
plt.grid(True)

# přidání legendy
plt.legend(loc="lower right")

# zobrazení grafu
plt.show()
