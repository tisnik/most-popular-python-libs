# Výpočet a vykreslení všech aktivačních funkcí
# Výpočet je proveden knihovnou PyTorch

import torch
import torch.nn as nn

import matplotlib.pyplot as plt

# velikost obrázku s grafem
plt.subplots(figsize=(6.4, 4.8))

# hodnoty na x-ové ose
x = torch.linspace(-5, 5, 100)

# výpočet všech tří aktivačních funkcí
relu = nn.ReLU()(x)
tanh = nn.Tanh()(x)
sigmoid = nn.Sigmoid()(x)

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
plt.savefig("activation_functions_pytorch.png")

# zobrazení v novém okně
plt.show()
