from scipy.stats import linregress

import numpy as np

import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.arange(0, 50)

# generátor pseudonáhodných dat
rng = np.random.default_rng(seed=42)

# hodnoty na y-ové ose
y = x + 10 * rng.random((len(x))) - 5

# výpočet lineární regrese
coefficients = linregress(x, y)

# koeficienty úsečky
print("Slope:", coefficients.slope)
print("Intercept:", coefficients.intercept)

# konstrukce lineární funkce
poly1d_fn = np.poly1d([coefficients.slope, coefficients.intercept])

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Lineární regrese", fontsize=15)

# vrcholy na křivce
ax.plot(x, y, "go")

# vykreslení interpolační křivky
plt.plot(poly1d_fn(np.arange(0, len(x))), "r-")

# popis os a legenda
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# uložení grafu do rastrového obrázku
plt.savefig("linear_regression_1.png")

# zobrazení grafu
plt.show()
