# Knihovna PyTorch
#
import torch

# konstrukce tenzoru, vyplneni sekvenci
v1 = torch.arange(1, 13)
print(v1)
print()

# vytvoreni matice z puvodniho vektoru
m1 = torch.reshape(v1, (4, 3))
print(m1)
print()

# jednorozmerny vektor
v2 = torch.Tensor([1, 2, -1])
print(v2)
print()

# nasobeni vektoru a matice prvek po prvku
m2 = v2 * m1
print(m2)
print()
