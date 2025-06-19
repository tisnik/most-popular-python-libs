# Knihovna PyTorch
#
# - výpočet a vykreslení aktivační funkce sigmoid
# - výpočet je proveden knihovnou PyTorch
# - vykreslení je provedeno knihovnou Matplotlib

import torch
import torch.nn as nn

import matplotlib.pyplot as plt

# velikost obrázku s grafem
plt.subplots(figsize=(6.4, 4.8))

# hodnoty na x-ové ose
x = torch.linspace(-5, 5, 100)

# výpočet aktivační funkce
y = nn.Sigmoid()(x)

# vykreslení aktivační funkce
plt.plot(x, y, label="Sigmoid")

# zobrazení legendy
plt.legend()

# zobrazení mřížky
plt.grid()

# uložení do souboru
plt.savefig("activation_function_sigmoid_pytorch.png")

# zobrazení v novém okně
plt.show()
