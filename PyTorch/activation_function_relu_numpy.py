# Knihovna PyTorch
#
# - výpočet a vykreslení aktivační funkce ReLU
# - výpočet je proveden knihovnou NumPy
# - vykreslení je provedeno knihovnou Matplotlib

import matplotlib.pyplot as plt
import numpy as np

# velikost obrázku s grafem
plt.subplots(figsize=(6.4, 4.8))

# hodnoty na x-ové ose
x = np.linspace(-5, 5, 100)

# výpočet aktivační funkce
y = [max(0, i) for i in x]

# vykreslení aktivační funkce
plt.plot(x, y, label="ReLU")

# zobrazení legendy
plt.legend()

# zobrazení mřížky
plt.grid()

# uložení do souboru
plt.savefig("activation_function_relu_numpy.png")

# zobrazení v novém okně
plt.show()
