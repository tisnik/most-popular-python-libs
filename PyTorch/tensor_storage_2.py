# Knihovna PyTorch
#
# - získání datové struktury se zdrojem dat pro tenzor

import torch

# konstrukce tenzoru druheho radu
m2 = torch.tensor([[1,2,3], [4,5,6]]).type(torch.uint8)
print(m2)
print(type(m2))
print(m2.dtype)

print()

# informace o typu Storage
storage = m2.untyped_storage()

print(storage)
print(type(storage))
