import torch

# konstrukce tenzoru
v1 = torch.arange(10, 20)
print("v1:")
print(v1)
print("Stride:", v1.stride())
print("Offset:", v1.storage_offset())
print()

# konstrukce tenzoru
m1 = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print("m1:")
print(m1)
print("Stride:", m1.stride())
print("Offset:", m1.storage_offset())
print()

# 3D struktura
m3 = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 20, 30], [40, 50, 60], [70, 80, 90]]]

# konstrukce tenzoru tretiho radu
c1 = torch.Tensor(m3)
print("c1:")
print(c1)
print("Stride:", c1.stride())
print("Offset:", c1.storage_offset())
