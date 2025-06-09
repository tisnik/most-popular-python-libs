# Knihovna PyTorch
#
import torch

# konstrukce tenzoru nulteho radu
v1 = torch.tensor(10, dtype=torch.bfloat16)
print(v1)
print(type(v1))
print(v1.dtype)

print()

# konstrukce tenzoru prvniho radu
v2 = torch.arange(10, 20).type(torch.bfloat16)
print(v2)
print(type(v2))
print(v2.dtype)

print()

# konstrukce tenzoru druheho radu se zmenou typu prvku
m1 = torch.Tensor(3, 4).type(torch.bfloat16)
print(m1)
print(type(m1))
print(m1.dtype)
