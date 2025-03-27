# Vykresleni ruznych aktivacnich funkci knihovnou PyTorch

import torch
import torch.nn as nn

import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = torch.linspace(-4, 4, 200)

# výpočet hodnot aktivačních funkcí
relu = nn.ReLU()(x)
tanh = nn.Tanh()(x)
sigmoid = nn.Sigmoid()(x)
 
# nový graf s průběhem tří aktivačních funkcí
plt.plot(x, sigmoid, label="sigmoid")
plt.plot(x, tanh, label="tanh")
plt.plot(x, relu, label="ReLU")
plt.ylim(-1.5, 2)

# zobrazení legendy
plt.legend()

# uložení do souboru
plt.savefig("activation_functions.png")

# zobrazení v novém okně
plt.show()
