from scipy.optimize import curve_fit

import numpy as np

import matplotlib.pyplot as plt


def func(x, a, b):
    return a * x + b


# hodnoty na x-ové ose
x = np.arange(0, 50)

# generátor pseudonáhodných dat
rng = np.random.default_rng(seed=42)

# hodnoty na y-ové ose
y = x + 10 * rng.random((len(x))) - 5

# vykreslení bodů
plt.plot(x, y, "go", label="data")

# výpočet koeficientů a a b
popt, pcov = curve_fit(func, x, y)

# koeficienty úsečky
print("Slope:", popt[0])
print("Intercept:", popt[1])

# vykreslení křivky prokládající body
plt.plot(x, func(x, *popt), "r-", label="fit: a=%5.3f, b=%5.3f" % tuple(popt))

# popis os a legenda
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# uložení grafu do rastrového obrázku
plt.savefig("curve_fit_1.png")

# zobrazení grafu
plt.show()
