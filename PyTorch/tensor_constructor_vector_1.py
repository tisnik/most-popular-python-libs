# Knihovna PyTorch
#
# - konstrukce tenzoru prvního řádu (tříprvkový vektor)

import torch

# konstrukce tenzoru prvniho radu (vektoru)
v1 = torch.Tensor(3)
print(v1)

# inicializace jednotlivych prvku vektoru
v1[0] = 10
v1[1] = 20
v1[2] = 30
print(v1)
