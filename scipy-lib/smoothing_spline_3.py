from scipy.interpolate import make_smoothing_spline

import numpy as np

import matplotlib.pyplot as plt


def func(x, a, b):
    return a * x + b


# hodnoty na x-ové ose
x = np.arange(0, 50)

# generátor pseudonáhodných dat
rng = np.random.default_rng(seed=42)

# hodnoty na y-ové ose
y = x + 20 * rng.random((len(x))) - 10

# vykreslení bodů
plt.plot(x, y, "go", label="data")

# vytvoření spline
spline1 = make_smoothing_spline(x, y, lam=0)
spline2 = make_smoothing_spline(x, y, lam=0.5)
spline3 = make_smoothing_spline(x, y, lam=10)

x = np.arange(0, 50, 0.5)

# vykreslení křivky
plt.plot(x, spline1(x), "r-", label="Spline 1")
plt.plot(x, spline2(x), "g-", label="Spline 2")
plt.plot(x, spline3(x), "b-", label="Spline 2")

# popis os a legenda
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# uložení grafu do rastrového obrázku
plt.savefig("smoothing_spline_3.png")

# zobrazení grafu
plt.show()
