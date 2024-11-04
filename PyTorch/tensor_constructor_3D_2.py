import torch

# 3D struktura
m3 = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 20, 30], [40, 50, 60], [70, 80, 90]]]

# konstrukce tenzoru tretiho radu
c = torch.Tensor(m3)
print(c)
