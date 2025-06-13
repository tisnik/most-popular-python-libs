# Knihovna PyTorch
#
# - konstrukce tenzoru
# - vyplnění nulami

import torch

# konstrukce tenzoru prvniho radu, vyplneni nulami
v1 = torch.zeros(1)
print(v1)
print()

# konstrukce tenzoru prvniho radu, vyplneni nulami
v2 = torch.zeros(10)
print(v2)
print()

# konstrukce tenzoru druheho radu, vyplneni nulami
m1 = torch.zeros(3, 4)
print(m1)
print()

# konstrukce tenzoru tretiho radu, vyplneni nulami
c1 = torch.zeros(3, 4, 5)
print(c1)
print()
