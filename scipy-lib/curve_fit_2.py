from scipy.optimize import curve_fit

import numpy as np

import matplotlib.pyplot as plt


def func(x, a, b, c):
    return a * x**2 + b*x + c


# hodnoty na x-ové ose
x = np.linspace(0, 4, 50)

# generátor pseudonáhodných dat
rng = np.random.default_rng(seed=42)

# hodnoty na y-ové ose
y_orig = func(x, 1.0, -1.5, 0.5)
y_noise = 0.2 * rng.normal(size=x.size)
y = y_orig + y_noise

# vykreslení bodů
plt.plot(x, y, "go", label="data")

# výpočet koeficientů a a b
popt, pcov = curve_fit(func, x, y)

# vykreslení křivky prokládající body
plt.plot(x, func(x, *popt), "r-", label="fit: a=%5.3f, b=%5.3f, c=%5.3f" % tuple(popt))

# popis os a legenda
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# uložení grafu do rastrového obrázku
plt.savefig("curve_fit_2.png")

# zobrazení grafu
plt.show()
