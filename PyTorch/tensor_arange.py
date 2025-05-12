# Knihovna PyTorch
#
import torch

# konstrukce tenzoru, vyplneni sekvenci
v1 = torch.arange(10, 20)
print(v1)

# specifikace kroku
v2 = torch.arange(10, 20, 2)
print(v2)

# zaporny krok
v3 = torch.arange(10, 0, -1)
print(v3)

# krok, ktery neni celociselny
v4 = torch.arange(0, 10, 0.5)
print(v4)

