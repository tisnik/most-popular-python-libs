# Knihovna PyTorch
#
# - konstrukce tenzoru prvního řádu s využitím generátoru range

import torch

# konstrukce tenzoru prvniho radu (tenzoru)
# s inicializací výsledkem generátoru range
v3 = torch.Tensor(range(10))
print(v3)
