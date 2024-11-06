import torch

# konstrukce tenzoru
m1 = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(m1)

print()

# konstrukce rezu - pres radky
m2 = m1[1:3]
print(m2)

print()

# konstrukce rezu - pres sloupce
m3 = m1[:,1:3]
print(m3)
