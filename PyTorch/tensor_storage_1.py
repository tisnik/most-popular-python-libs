# Knihovna PyTorch
#
# - získání datové struktury se zdrojem dat pro tenzor

import torch

# konstrukce tenzoru prvniho radu
v1 = torch.tensor([1, 255, 65535, 65536])
print(v1)
print(type(v1))
print(v1.dtype)

print()

# informace o typu Storage
storage = v1.untyped_storage()

print(storage)
print(type(storage))
