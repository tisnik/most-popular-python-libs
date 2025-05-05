# Knihovna PyTorch
#
# - výpočet a vykreslení aktivační funkce tanh
# - výpočet je proveden knihovnou PyTorch
# - vykreslení je provedeno knihovnou Matplotlib

import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import numpy as np

# velikost obrázku s grafem
plt.subplots(figsize=(6.4, 4.8))

# hodnoty na x-ové ose
x = torch.linspace(-5, 5, 100)

# výpočet aktivační funkce
y = nn.Tanh()(x)

# vykreslení aktivační funkce
plt.plot(x, y, label="Tanh")

# zobrazení legendy
plt.legend()

# zobrazení mřížky
plt.grid()

# uložení do souboru
plt.savefig("activation_function_tanh_pytorch.png")

# zobrazení v novém okně
plt.show()
