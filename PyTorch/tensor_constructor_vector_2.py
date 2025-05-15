# Knihovna PyTorch
#
import torch

# konstrukce tenzoru prvniho radu (vektoru) s inicializaci prvku
v2 = torch.Tensor([1, 2, 3])
print(v2)

# pristup k (jedine) slozce tenzoru
v2[0] = 10
v2[1] = 20
v2[2] = 30
print(v2)
