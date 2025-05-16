# Knihovna PyTorch
#
import torch

# konstrukce tenzoru
v1 = torch.arange(10, 20)
print(v1)

# konstrukce rezu
v2 = v1[5:10]
print(v2)

# modifikace vektoru
v1[5] = 999
print(v1)
print(v2)

# modifikace rezu
v2[0] = 0
print(v1)
print(v2)
