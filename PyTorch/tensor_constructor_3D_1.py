# Knihovna PyTorch
#
import torch

# 2D struktury - matice
m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

# konstrukce tenzoru tretiho radu
c = torch.Tensor([m1, m2])
print(c)
