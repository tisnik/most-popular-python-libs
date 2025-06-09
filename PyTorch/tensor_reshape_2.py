# Knihovna PyTorch
#
import torch

# konstrukce tenzoru
m1 = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(m1)
print()

v1 = torch.reshape(m1, (16, ))
print(v1)
