# Knihovna PyTorch
#
# - získání datové struktury se zdrojem dat pro tenzor

import torch

# konstrukce tenzoru tretiho radu
c1 = torch.tensor([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]]).type(torch.int16)
print(c1)
print(type(c1))
print(c1.dtype)

print()

# informace o typu Storage
storage = c1.untyped_storage()

print(storage)
print(type(storage))
