import torch

# konstrukce tenzoru, vyplneni sekvenci
v1 = torch.range(10, 20)
print(v1)

# specifikace kroku
v2 = torch.range(10, 20, 2)
print(v2)

# zaporny krok
v3 = torch.range(10, 0, -1)
print(v3)

# krok, ktery neni celociselny
v4 = torch.range(0, 10, 0.5)
print(v4)

