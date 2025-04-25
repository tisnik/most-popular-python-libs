# Knihovna PyTorch
#
# - výpočet a vykreslení aktivační funkce sigmoid
# - výpočet je proveden knihovnou NumPy
# - vykreslení je provedeno knihovnou Matplotlib

import matplotlib.pyplot as plt
import numpy as np

# velikost obrázku s grafem
plt.subplots(figsize=(6.4, 4.8))

# hodnoty na x-ové ose
x = np.linspace(-5, 5, 100)

# výpočet aktivační funkce
y = 1/(1 + np.exp(-x))

# vykreslení aktivační funkce
plt.plot(x, y, label="Sigmoid")

# zobrazení legendy
plt.legend()

# zobrazení mřížky
plt.grid()

# uložení do souboru
plt.savefig("activation_function_sigmoid_numpy.png")

# zobrazení v novém okně
plt.show()
