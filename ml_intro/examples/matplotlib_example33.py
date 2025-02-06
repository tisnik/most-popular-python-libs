# - vykreslení průběhu exponenciální funkce
# - při vykreslování se jednotlivé body spojí úsečkami
# - v ose x i y se použije logaritmické měřítko

import matplotlib.pyplot as plt
import numpy as np

# hodnoty na x-ové ose
x = np.linspace(0.0, 10.0, 1000)

# hodnoty na y-ové ose
y = 2 ** x

# vykreslit průběh funkce
plt.plot(x, y, color="blue", label="exp(x)")

# logaritmické měřítko v ose x
plt.xscale("log")

# logaritmické měřítko v ose y
plt.yscale("log")

# povolení zobrazení mřížky
plt.grid(True)

# popis os
plt.xlabel("x")
plt.ylabel("exp(x)")

# přidání legendy
plt.legend(loc="upper left")

# zobrazení grafu
plt.show()
