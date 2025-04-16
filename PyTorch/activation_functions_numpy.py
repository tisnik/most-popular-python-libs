# Výpočet a vykreslení všech aktivačních funkcí
# Výpočet je proveden knihovnou NumPy

import matplotlib.pyplot as plt
import numpy as np

# velikost obrázku s grafem
plt.subplots(figsize=(6.4, 4.8))

# hodnoty na x-ové ose
x = np.linspace(-5, 5, 100)

# výpočet všech tří aktivačních funkcí
relu = [max(0, i) for i in x]
tanh = np.tanh(x)
sigmoid = 1/(1 + np.exp(-x))

# vykreslení všech tří aktivačních funkcí
plt.plot(x, sigmoid, label="sigmoid")
plt.plot(x, tanh, label="tanh")
plt.plot(x, relu, label="ReLU")
plt.ylim(-1.5, 2)

# zobrazení legendy
plt.legend()

# zobrazení mřížky
plt.grid()

# uložení do souboru
plt.savefig("activation_functions_numpy.png")

# zobrazení v novém okně
plt.show()
