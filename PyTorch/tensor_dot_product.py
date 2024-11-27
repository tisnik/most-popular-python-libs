import torch

# konstrukce 1D tenzoru
v1 = torch.Tensor([2, 2, 3, 5])
print(v1)
print()

# konstrukce druheho 2D tenzoru
v2 = torch.Tensor([2, 2, 3, 5])
print(v2)
print()

# skalarni soucin zapsany funkci
s = torch.dot(v1, v2)
print(s)
print()

# skalarni soucin zapsany operatorem
s = v1 @ v2
print(s)

# vysledkem je 42 - nahoda???
