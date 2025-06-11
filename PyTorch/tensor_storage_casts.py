# Knihovna PyTorch
#
# - přetypování datové struktury se zdrojem dat pro tenzor

import torch

# konstrukce tenzoru
v1 = torch.tensor(10)
print(v1)
print(type(v1))
print(v1.dtype)

print()

storage = v1.untyped_storage()

print(storage.int())
print(storage.half())
print(storage.float())
print(storage.double())
