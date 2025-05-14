# Knihovna PyTorch
#
import torch

# skutecny skalar - tenzor nulteho radu
s1 = torch.tensor(100)
print(s1)

# konstrukce tenzoru prvniho radu (jednoprvkovy vektor)
s2 = torch.Tensor(1)
print(s2)

# pristup k (jedine) slozce tenzoru
s2[0] = 42
print(s2)
