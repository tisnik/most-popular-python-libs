from scipy.interpolate import CubicSpline

import numpy as np

import matplotlib.pyplot as plt


# hodnoty na x-ové ose
x = np.arange(0, 10)

# generátor pseudonáhodných dat
rng = np.random.default_rng(seed=42)

# hodnoty na y-ové ose
y = x + 10 * rng.random((len(x))) - 5

# vykreslení bodů
plt.plot(x, y, "go", label="data")

# vytvoření spline
spline = CubicSpline(x, y)

x = np.arange(0, 10, 0.01)

# vykreslení křivky
plt.plot(x, spline(x), "r-", label="Spline")
plt.plot(x, spline(x, nu=1), '--', label='1st derivative')

# popis os a legenda
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# uložení grafu do rastrového obrázku
plt.savefig("cubic_spline_2.png")

# zobrazení grafu
plt.show()
