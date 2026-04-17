from scipy.interpolate import CubicSpline
from scipy.interpolate import make_smoothing_spline

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
spline1 = CubicSpline(x, y)
spline2 = make_smoothing_spline(x, y, lam=0)
spline3 = make_smoothing_spline(x, y, lam=0.5)
spline4 = make_smoothing_spline(x, y, lam=10)

x = np.arange(0, 10, 0.01)

# vykreslení křivek
plt.plot(x, spline1(x), "r-", label="Cubic spline")

plt.plot(x, spline2(x), "b-", label="Smoothing spline #1")
plt.plot(x, spline3(x), "g-", label="Smoothing spline #2")
plt.plot(x, spline4(x), "y-", label="Smoothing spline #3")

# popis os a legenda
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# uložení grafu do rastrového obrázku
plt.savefig("comparison_2.png")

# zobrazení grafu
plt.show()
