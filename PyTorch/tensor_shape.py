# Knihovna PyTorch
#
import torch

# konstrukce tenzoru + zjisteni jejich tvaru

# tenzor nulteho radu - skalar
s1 = torch.tensor(100)
print(s1.shape)

# tenzor prvniho radu - vektor
v1 = torch.Tensor(1)
print(v1.shape)

v2 = torch.Tensor(3)
print(v2.shape)

# tenzor druheho radu - matice
m1 = torch.Tensor(3, 4)
print(m1.shape)

# tenzor tretiho radu - 3D pole
c1 = torch.Tensor(3, 4, 5)
print(c1.shape)
