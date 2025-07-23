# Knihovna PyTorch
#
# - zjištění, jakého typu jsou prvky tenzoru

import torch

# konstrukce tenzoru
v1 = torch.tensor(10)
print(v1)
print(type(v1))
print(v1.dtype)
