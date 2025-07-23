# Knihovna PyTorch
#
# - změna tvaru tenzoru operací reshape

import torch

# konstrukce tenzoru, vyplneni sekvenci
v1 = torch.range(1, 12)
print(v1)
print()

m1 = torch.reshape(v1, (4, 3))
print(m1)
print()

m2 = torch.reshape(v1, (3, 4))
print(m2)
print()

m3 = torch.reshape(v1, (3, 2, 2))
print(m3)
print()

m4 = torch.reshape(v1, (2, 3, 2))
print(m4)
print()

m5 = torch.reshape(v1, (2, 2, 3))
print(m5)
print()
