# Knihovna PyTorch
#
# - inicializace tenzoru prvního řádu s jedním prvkem

import torch

# konstrukce tenzoru (jednoprvkovy vektor) s jeho inicializaci
s2 = torch.tensor([-1])
print(s2)

# pristup k (jedine) slozce tenzoru
s2[0] = 42
print(s2)
