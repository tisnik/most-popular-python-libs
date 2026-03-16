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
spline = make_smoothing_spline(x, y)

# vykreslení křivky
plt.plot(x, spline(x), "r-", label="Spline")

# popis os a legenda
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# uložení grafu do rastrového obrázku
plt.savefig("smoothing_spline_2.png")

# zobrazení grafu
plt.show()
