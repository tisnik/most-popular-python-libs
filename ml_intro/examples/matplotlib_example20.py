# - sloupcový graf se dvěma skupinami sloupců
#   a se zobrazením odchylek

import matplotlib.pyplot as plt
import numpy as np

# první pole hodnot a pole odchylek
vals1 = [10, 15, 20, 12, 14, 8]
delta1 = [1, 2, 3, 4, 5, 0]

# druhé pole hodnot a pole odchylek
vals2 = [19, 18, 6, 11, 6, 14]
delta2 = [4, 2, 3, 2, 2, 4]

# počet prvků
N = len(vals1)

# indexy prvků
indexes = np.arange(N)

# šířka sloupců
width = 0.30

# sloupcový graf se dvěma skupinami sloupců
plt.bar(
    indexes,
    vals1,
    width,
    color="gray",
    edgecolor="black",
    label="CPU#1",
    yerr=delta1,
    error_kw=dict(elinewidth=2, ecolor="red"),
)

# posunuté sloupce
plt.bar(
    indexes + width,
    vals2,
    width,
    color="red",
    edgecolor="black",
    label="CPU#2",
    yerr=delta2,
    error_kw=dict(elinewidth=2, ecolor="black"),
)

# povolení zobrazení mřížky
plt.grid(True)

# přidání legendy
plt.legend(loc="lower right")

# zobrazení grafu
plt.show()
